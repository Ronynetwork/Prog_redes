from var import *
from otherfunc import *
from functions_download import *
from run import *
import time
#-------------------------------------------------------------------------------------------------------------------------------------------------

#                                                          PARTE CLIENTE                                                                     #

def user_interaction(sock):
    msg = b''
    try:
        while msg != '/q':
            time.sleep(0.3)
            msg = input(PROMPT).lower()
            if not msg.strip():  # Verifica se a string contém apenas espaços em branco
                comunicacao = '\nVocê enviou uma mensagem vazia, tente inserir /? para obter ajuda sobre os serviços disponíveis\n'
                PRINTS(comunicacao)

            else:
                sock.send(msg.encode(CODE))

    except:
        exit()
    finally:
        PRINTS("Voce solicitou o fim da conexao, ate a proxima!!")        

def server_interaction(sock):
    try:
        msg = b''

        while True:
            msg = sock.recv(4096)
            msg_decode = msg.decode(CODE)

            if msg_decode == 'exit':  # Se a mensagem estiver vazia, significa que o servidor encerrou a conexão.
                break
            # Converte os bytes de volta para uma string
            print(msg_decode)
            
    except Exception as exceção:
        print(f'Erro na comunicação com o servidor: {exceção}')
    finally:
        ServerLog.critical('O cliente solicitou o fim da conexao')
        sock.close()

#                                                        PARTE DO SERVIDOR                                                                  #
# -----------------------------------------------------------------------------------------------------------------------------------------------

def conn_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((SERVER, PORT))
        PRINTS(f'\nServidor {SERVER} a espera de conexões na porta {PORT}!\n')
        server.listen()
        
        return server
    except:
        ServerLog.eror(f'Erro ao estabelecer a conexão do servidor{sys.exc_info()[0]}')
        server.close()
  

# -----------------------------------------------------------------------------------------------------------------------------------------------

#                                                    FUNÇÕES INTERATIVAS DO SERVIDOR                                                        #

def broadCast(clients_list, client_info, comunicacao):
    comunicacao_div = SPLIT(comunicacao)
    message = comunicacao_div[1]
    msg = f'\nO cliente: {client_info} Enviou uma mensagem para todos!\nMensagem > {message}'
    try:
        for key, value in clients_list.items():
            if key != client_info[1]:
                sock_broadcast = value[1]
                sock_broadcast.send(msg.encode(CODE))
        ServerLog.info('Foi solicitado o comando /b -> enviar mensagem em broadcast.')
        ServerLog.info(f'A mensagem enviada via broadcast foi {message}')
    except:
        ServerLog.error(f'Erro ao enviar mensagem em Broadcast... {sys.exc_info()[0]}')
        exit()

# -----------------------------------------------------------------------------------------------------------------------------------------------

#                                   função que envia uma mensagem do cliente para outro em específico                                         #

def Private(socket_client, msg, clients_list):
    comunicacao = SPLIT(msg)
    socket_source = socket_client.getpeername()
    dest_client = (comunicacao[1], int(comunicacao[2]))
    msg = f'\nMensagem recebida: \n{socket_source}: {comunicacao[3]}'

    for key, value in clients_list.items():
        try:
            # Verifica se o IP e a porta correspondem ao cliente destino
            if key == dest_client[1]:
                sock_dest = value[1]
                # Envia a mensagem para o endereço do cliente destinatário
                sock_dest.send(msg.encode(CODE))
                ServerLog.info('Foi solicitado o comando /m -> mensagem privada.')
                ServerLog.info(f'O cliente: {dest_client} recebeu uma mensagem -> {msg}')

        except Exception as e:
            error_message = f'Não foi possível localizar o cliente informado... {str(e)}'
            socket_client.send(error_message.encode(CODE))
            ServerLog.error(f'erro na função Private: {str(e)}')
# -----------------------------------------------------------------------------------------------------------------------------------------------

#                             FUNÇÃO QUE PRINTA TODOS OS COMANDOS E MENSAGENS TROCADAS ENTRE O CLIENTE E O SERVIDOR       #               

def HISTORY(historic, socket_client):
    try:
        msg = f'\nEsse é seu histórico de comandos:\n' 
        for qtd, comando in enumerate(historic, start=1):
            msg += f'{qtd} {comando}\n'
               
        ServerLog.info('Foi solicitado o comando /h -> Historico de mensagens.')
        socket_client.send(msg.encode(CODE))

    except:
        ServerLog.error(f'Erro no envio do History... {sys.exc_info()[0]}')
# -------------------------------------------------------------------------------------------------------------------------------------------------

#                                           FUNÇÃO QUE LISTA TODOS OS CLIENTES CONECTADOS NO SERVIDOR                                         #

def List_Clients(clients_list, socket_client):
    try: 
        num = 0
        msg = f'\nEsses são os clientes conectados:\n'
        for chave, valor in clients_list.items():  # faço um for para pegar cada cliente conectado e enviar  
            num +=1 # formatação numeração cliente
            msg += f"\nCLIENTE {num}\nIP: {valor[0]}\nPORT: {chave}\n" # formatação listagem clientes (lembrando que chave=porta e valor[0]=ip)
        
        ServerLog.info('Foi solicitado o comando /l -> Listagem dos clientes conectados no servidor.')
        socket_client.send(msg.encode(CODE)) # enviando mensagens 
    except:
        ServerLog.error(f'Erro no momento de Listar os Clientes Conectados...{sys.exc_info()[0]}')  
        exit()
# -------------------------------------------------------------------------------------------------------------------------------------------------

#                                               FUNÇÃO QUE REMOVE O CLIENTE CONECTADO NO SERVIDOR                                                 #

def desconnect(clients_list, client_info, socket_client):
    try:
        ServerLog.critical(f'O cliente: {client_info} solicitou o fim da conexão.')
        
        # Remove o cliente da lista de clientes
        if client_info[1] in clients_list:
            msg_exit = 'exit'
            del clients_list[client_info[1]]
            ServerLog.info(f'Cliente {client_info} removido com sucesso.')
            socket_client.send(msg_exit.encode(CODE))

        else:
            ServerLog.warning(f'Cliente {client_info} não encontrado na lista.')

        # Fecha o socket do cliente
        socket_client.close()
        ServerLog.info(f'Socket do cliente {client_info} fechado com sucesso.')

    except Exception as e:
        ServerLog.error(f'Erro no momento de remover o cliente {client_info}: {e}')

    finally:
        # Garantir que o processo ou a thread termine
        sys.exit()
# -------------------------------------------------------------------------------------------------------------------------------------------------

#                                      FUNÇÃO QUE EXPLICA A FUNCIONALIDADE DE TODAS AS OUTRAS FUNÇÕES                                         #
def HELP(socket_client):
    try:
        # Criando descrição de cada comando
        options = {
        '/l': 'Listar os clientes conectados',
        '/m:ip:porta:mensagem': 'Enviar mensagem para um cliente especifíco (informe IP:PORTA do cliente) depois digite sua mensagem',
        '/b:mensagem': 'Enviar mensagem para todos clientes conectados',
        '/h': 'Lista o seu histórico de comandos',
        '/?': 'Lista as opções disponiveis',
        '/q': 'Desconectar do Servidor',
        '/d:nome_do_arquivo': 'Enviar arquivo do servidor para o cliente',
        '/w:url': 'Efetuar o download de um arquivo a partir da url informada',
        '/u:nome_arquivo': 'Enviar um arquivo para o servidor\n'
        }
        title = f"\nSegue abaixo as Opções disponiveis neste servidor:"
        socket_client.send(title.encode(CODE))
        for com, describ in options.items(): # listando por meio do FOR comando por comando 
            help_com = f"\n{com} -> {describ}" # formatação mensagem
            socket_client.send(help_com.encode(CODE)) # enviando comando por comando
        ServerLog.info('Foi solicitado o comando /? -> Listagem dos comandos do servidor.')

    except:
        ServerLog.error(f'Erro ao listar as Opções...{sys.exc_info()[0]}')  
        exit()  
# -------------------------------------------------------------------------------------------------------------------------------------------------

# -------------------------------------------------------------------------------------------------------------------------------------------------
'''                                             FUNÇÃO QUE LISTA OS ARQUIVOS PRESENTES EM SERVER_FILES                                          '''
def Server_files(socket_client):
    try:
        local =  os.path.dirname(os.path.abspath(__file__)) + '\\server_files\\'
        # Obtém a lista de itens (arquivos e diretórios) no diretório especificado
        itens_no_diretorio = os.listdir(local)
        msg = f'\nEstes são os arquivos presentes na pasta do servidor e seus respectivos tamanhos:\n' + '-'*50 + '\n'
        # Filtra apenas os arquivos
        for item in itens_no_diretorio:
            lenght = os.path.getsize(local+item)
            msg += f'({item}): {lenght} bytes;\n'
        arqs= msg + '-' * 50
        socket_client.send(arqs.encode(CODE))
        socket_client.send('Caso deseje realizar o download de algum arquivo, por favor utilizar o comando (/d:(nome do arquivo)).\n'.encode(CODE))
        ServerLog.info('Foi solicitado o comando /f -> Listagem dos arquivos do servidor.')

    except FileNotFoundError:
        ServerLog.debug("Diretório não encontrado.")


#-------------------------------------------------------------------------------------------------------------------------------------------------

#                                       INTERAÇÃO ENTRE AS MENSAGENS RECEBIDAS E OS COMANDOS ENVIADOS                                        #

def Client_Interaction(socket_client, client_info, clients_list):
    try:
        historic = list()

        while True:
            comunicacao = socket_client.recv(1024).decode(CODE).lower()
            command = SPLIT(comunicacao)
            historic.append(command[0])

            if command[0] == '/?':
                HELP(socket_client)
            elif command[0] == '/q':
                desconnect(clients_list, client_info, socket_client)
            elif command[0] == '/b':
                broadCast(clients_list, client_info, comunicacao)
            elif command[0] == '/f':
                Server_files(socket_client)
            elif command[0] == '/h':
                HISTORY(historic, socket_client)
            elif command[0] == '/l':
                List_Clients(clients_list, socket_client)
            elif command[0] == '/m':
                Private(socket_client, comunicacao, clients_list)
            elif command[0] == '/w':
                DOWNLOAD(socket_client, comunicacao)

            else:
                ServerLog.info(f'O cliente(IP/PORTA): ({client_info[0]}, {client_info[1]}) -> enviou uma mensagem: {command[0]}')

    except Exception as e:
        PRINTS(f'Erro... {e}')