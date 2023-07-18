from variables import *
import sys, socket
# -----------------------------------------------------------------------------------------------------------------------------------------------

def PRINTS(x):
    print('-'*100)
    print(x)
    print('-'*100)

# -----------------------------------------------------------------------------------------------------------------------------------------------

def SPLIT(comunicacao):
    try:
        com_split = comunicacao.split(':')
    except:
        print(f'Erro ao desmembrar a mensagem... {sys.exc_info()[0]}')

# -----------------------------------------------------------------------------------------------------------------------------------------------

def conn_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((SERVER, PORT))
        PRINTS(f'\nServidor {SERVER} a espera de conexões na porta {PORT}!\n')
        server.listen(6)

        return server

    except:
        print(f'Erro ao estabaelecer a conexão do servidor{sys.exc_info()}')
        server.close()       

# -----------------------------------------------------------------------------------------------------------------------------------------------

'''                                                    FUNÇÕES INTERATIVAS DO SERVIDOR                                                        '''

def broadCast(comunicacao, clients):
    comunicacao = SPLIT(comunicacao)
    
    for x in clients:
        try:
            conn.send(comunicacao[1].encode(CODE))
        except:
            print(f'Erro ao enviar a mensagem... {sys.exc_info()[0]}')

# -----------------------------------------------------------------------------------------------------------------------------------------------

def HISTORY(comunicacao):
    mensagens = []
    prim_command = (sys.argv[0].split('/')[-1])
    mensagens.append(prim_command)  
    while True:
        comunicacao = input('Insira uma mensagem:')
        if comunicacao == 'quit':
            break
        if comunicacao != 'quit':
            mensagens.append(comunicacao)
        else:
            PRINTS(f'Sua histórico de mensagens: {mensagens}')

# -------------------------------------------------------------------------------------------------------------------------------------------------
'''                                           FUNÇÃO QUE LISTA TODOS OS CLIENTES CONECTADOS NO SERVIDOR                                         '''

def List_Clients(clients, sock, **kwargs):
    try: 
        msg_title = "\nOs Clientes conectados ao Servidor são:" # formatando mensagem 
        sock.send(msg_title.encode(CODE)) 
        num = 0
        for chave, valor in clients.items():  # faço um for para pegar cada cliente conectado e enviar 
            ip = valor[0] # Armazenamento Temporário 
            num+=1 # formatação numeração cliente
            msg_list = f"\nCLIENTE {num}\nIP: {ip}\nPORT: {chave}\n" # formatação listagem clientes (lembrando que chave=porta e valor[0]=ip)
            sock.send(msg_list.encode(CODE)) # enviando mensagens 
    except:
        print(f'\nErro no momento de Listar os Clientes Conectados...{sys.exc_info()[0]}')  
        exit()
        
# -------------------------------------------------------------------------------------------------------------------------------------------------
'''                                      FUNÇÃO QUE EXPLICA A FUNCIONALIDADE DE TODAS AS OUTRAS FUNÇÕES                                         '''
def HELP(sock, **kwargs):
    try:
        # Criando descrição de cada comando
        descriptive_options = {
        '/l': 'Listar os clientes conectados',
        '/m:ip:porta:mensagem': 'Enviar mensagem para um cliente especifíco (informe IP:PORTA do cliente) depois digite sua mensagem',
        '/b:mensagem': 'Enviar mensagem para todos clientes conectados',
        '/h': 'Lista o seu histórico de comandos',
        '/?': 'Lista as opções disponiveis',
        '/q': 'Desconectar do Servidor'
        }
        msg_title = f"\nSegue abaixo as Opções disponiveis neste servidor:"
        sock.send(msg_title.encode(CODE))
        for comando, descrição in descriptive_options.items(): # listando por meio do FOR comando por comando 
            msg_help = f"\n{comando} -> {descrição}\n" # formatação mensagem
            sock.send(msg_help.encode(CODE)) # enviando comando por comando
    except:
        PRINTS(f'\nErro ao listar as Opções...{sys.exc_info()[0]}')  
        exit()  
# -------------------------------------------------------------------------------------------------------------------------------------------------
'''                                   função que envia uma mensagem do cliente para outro em específico                                         '''

def Private(server, comunicacao, clients):
        comunicacao = SPLIT(comunicacao)
        for x in clients:
            try:
                if x == comunicacao[2]:
                    PRINTS('Enviando a mensagem para o cliente informado...\nAguarde.')
                    server.connect(comunicacao[1], comunicacao[2])
                    server.send(comunicacao[3])
                    print('Mensagem enviada com sucesso'), print('-'*100)
            except:
                PRINTS(f'Não foi possível localizar o cliente informado... {sys.exc_info()[0]}')

#-------------------------------------------------------------------------------------------------------------------------------------------------
'''                                       INTERAÇÃO ENTRE AS MENSAGENS RECEBIDAS E OS COMANDOS ENVIADOS                                        '''

def Client_Interaction(server, client, end, clients):
    comunicacao = b''
    while comunicacao != b'/q':
        try:
            comunicacao = server.recv(BUFFER)
            commands = {'/?':HELP(),
            '/l':List_Clients(),
            '/m':Private(),
            '/b':broadCast()
            }
        except:
            print(f'Comando não encontrado. Erro({sys.exc_info()[0]})')
    else:
        comunicacao = b'/q'
        clients.remove ((server, end))
        client.close()