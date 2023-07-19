import sys, socket, threading

#                                          VARIÁVEIS                                                   <:

SERVER = '0.0.0.0'
PORT = 5678
PROMPT = 'Digite sua msg (!q para terminar) > '
CLIENT = 'localhost'
CODE = 'utf-8'
BUFFER = 512

#-------------------------------------------------------------------------------------------------------------------------------------------------

#                                                          PARTE CLIENTE                                                                     #

def closeSocket(sock):
    try:
        sock.close()
    except:
        None

#-------------------------------------------------------------------------------------------------------------------------------------------------
def server_interaction(sock):
    msg = b''
    while msg != b'':
        try:
            msg = sock.recv(512)
        except:
            msg = b''
            exit()

#-------------------------------------------------------------------------------------------------------------------------------------------------
def user_interaction(sock):
    msg = b''
    while msg != '/q':
        try:
            msg = input(PROMPT)
            if msg != '': sock.send(msg.encode('utf-8'))
        except:
            msg = '/q'
            exit()

#                                                        PARTE DO SERVIDOR                                                                  #
# -----------------------------------------------------------------------------------------------------------------------------------------------

def PRINTS(x):
    print('-'*100)
    print(x)
    print('-'*100)

# -----------------------------------------------------------------------------------------------------------------------------------------------

def SPLIT(x):
    try:
        comunicacao = x.split(':')
        return comunicacao
    except:
        print(f'Erro ao desmembrar a mensagem... {sys.exc_info()[0]}')

# -----------------------------------------------------------------------------------------------------------------------------------------------

def conn_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((SERVER, PORT))
        PRINTS(f'\nServidor {SERVER} a espera de conexões na porta {PORT}!\n')
        server.listen(5)
        
        return server

    except:
        print(f'Erro ao estabelecer a conexão do servidor{sys.exc_info()[0]}')
        server.close()
  

# -----------------------------------------------------------------------------------------------------------------------------------------------

#                                                    FUNÇÕES INTERATIVAS DO SERVIDOR                                                        #

def broadCast(clients_list, client_info, comunicacao):
    comunicacao_div = SPLIT(comunicacao)
    msg = f'O cliente: {client_info[0]} | {client_info[1]} Enviou uma mensagem para todos!\nMensagem > {comunicacao_div[1]}'
    try:
        for key, value in clients_list.items():
            if key != client_info[1]:
                sock_broadcast = value[1]
                sock_broadcast.send(msg.encode(CODE))
    except:
        print(f'Erro ao enviar mensagem em Broadcast... {sys.exc_info()[0]}')
        exit()

# -----------------------------------------------------------------------------------------------------------------------------------------------

#                             FUNÇÃO QUE PRINTA TODOS OS COMANDOS E MENSAGENS TROCADAS ENTRE O CLIENTE E O SERVIDOR       #               

def HISTORY(mensagens=None, sock= None, **kwargs):
    try:
        msg = f'Esse é seu histórico de comandos:\n\n'
        qtd = 0
        for x in mensagens:
            qtd +=1
            msg += f'{qtd} {x}\n'
        sock.send(msg.encode(CODE))
    except:
        print(f'Erro no envio do History... {sys.exc_info()[0]}')
# -------------------------------------------------------------------------------------------------------------------------------------------------

#                                           FUNÇÃO QUE LISTA TODOS OS CLIENTES CONECTADOS NO SERVIDOR                                         #

def List_Clients(clients=None, sock=None, **kwargs):
    try: 
        title = "\nOs Clientes conectados ao Servidor são:" # formatando mensagem 
        sock.send(title.encode(CODE)) 
        num = 0
        for chave, valor in clients.items():  # faço um for para pegar cada cliente conectado e enviar  
            num+=1 # formatação numeração cliente
            comunicacao_list = f"\nCLIENTE {num}\nIP: {valor[0]}\nPORT: {chave}\n" # formatação listagem clientes (lembrando que chave=porta e valor[0]=ip)
            sock.send(comunicacao_list.encode(CODE)) # enviando mensagens 
    except:
        print(f'\nErro no momento de Listar os Clientes Conectados...{sys.exc_info()[0]}')  
        exit()

# -------------------------------------------------------------------------------------------------------------------------------------------------

#                                      FUNÇÃO QUE EXPLICA A FUNCIONALIDADE DE TODAS AS OUTRAS FUNÇÕES                                         #
def HELP(sock=None, **kwargs):
    try:
        # Criando descrição de cada comando
        options = {
        '/l': 'Listar os clientes conectados',
        '/m:ip:porta:mensagem': 'Enviar mensagem para um cliente especifíco (informe IP:PORTA do cliente) depois digite sua mensagem',
        '/b:mensagem': 'Enviar mensagem para todos clientes conectados',
        '/h': 'Lista o seu histórico de comandos',
        '/?': 'Lista as opções disponiveis',
        '/q': 'Desconectar do Servidor'
        }
        title = f"\nSegue abaixo as Opções disponiveis neste servidor:"
        sock.send(title.encode(CODE))
        for com, describ in options.items(): # listando por meio do FOR comando por comando 
            help_com = f"\n{com} -> {describ}" # formatação mensagem
            sock.send(help_com.encode(CODE)) # enviando comando por comando
    except:
        PRINTS(f'\nErro ao listar as Opções...{sys.exc_info()[0]}')  
        exit()  
# -------------------------------------------------------------------------------------------------------------------------------------------------

#                                   função que envia uma mensagem do cliente para outro em específico                                         #

def Private(server, comunicacao, clients):
        comunicacao = SPLIT(comunicacao)
        for key, value in clients.items():
            try:
                if str(key) == comunicacao[2] and value[0] == comunicacao[1]:
                    PRINTS('Enviando a mensagem para o cliente informado...\nAguarde.')
                    
                    server.send((f'O cliente: {clients[0]}:{clients[1]} enviou uma mensagem para você.').encode(CODE))
            except:
                server.send((f'Não foi possível localizar o cliente informado... {sys.exc_info()[0]}').encode(CODE))

#-------------------------------------------------------------------------------------------------------------------------------------------------

#                                       INTERAÇÃO ENTRE AS MENSAGENS RECEBIDAS E OS COMANDOS ENVIADOS                                        #







def Client_Interaction(socket_client, client_info):
    mensagens = []
    msg = b''
    while msg != b'!q':
        try:
            msg = socket_client.recv(512)
            broadCast (msg, client_info)
        except:
            msg = b'!q'
    allSocks.remove ((sockConn, addr))
    sockConn.close()


'''def Client_Interaction(socket_client, client_info, client_list):
    try:
        commands = {
        '/?':HELP,
        '/l':List_Clients,
        '/m':Private,
        '/b':broadCast,
        '/h':HISTORY}
        commands_choice = set(commands.keys()) # usado para verificar se o comando pertence ao dicionário 
        mensagens = []
        comunicacao = b''
        while comunicacao != b'/q':
            try:
                comunicacao = socket_client.recv(512).decode(CODE)
                print(f'(IP:{client_info[0]}, PORTA:{client_info[1]}) -> {comunicacao}')
                mensagens.append(comunicacao)
                command = SPLIT(comunicacao)
                command_brute = command[0].lower()
                command_function = commands_choice.get(command_brute)
                if command_function: # Verifica se o comando existe no dicionário
                    # Executa a função associada ao comando
                    command_function(clients_list = client_list, socket_client = socket_client, comand=comunicacao[0], commands=commands, mensagens=mensagens, client_info=client_info)
                else:
                    # Caso o comando não exista no dicionário, você pode lidar com isso de acordo com o que for adequado para o seu caso.
                    print("Comando não encontrado!")
            except:
                comunicacao = b'/q'
        del client_list[client_info[1]]
        socket_client.close()
    except:
        print(f'Erro no Client_interaction...{sys.exc_info()[0]}')
'''









'''def Client_Interaction(sock, client_info, clients_list):
    try:
        commands = {
            '/?':HELP,
            '/l':List_Clients,
            
            '/h':HISTORY,}
        commands_choice = set(commands.keys()) # usado para verificar se o comando pertence ao dicionário 
        mensagens = []
        comunicacao = b''
        while comunicacao != b'/q':
            try:
                comunicacao = sock.recv(BUFFER).decode(CODE) # recebendo mensagem do cliente
                print(f'(IP:{client_info[0]}, PORTA:{client_info[1]}) -> {comunicacao}')
                mensagens.append(comunicacao)   
                comand = SPLIT(comunicacao) # realizando split do comando do cliente 
                command_brute = comand[0].lower() # usando apenas para pegar o comando bruto "/x"
            except:
                comunicacao = b'/q'
            del clients_list[client_info[1]] # quando o cliente digitar /q ele exclui socket do cliente da lista de clientes ativos
            sock.close()
            break
    except:
        print(f'Erro ao adicionar o cliente ao servidor...({sys.exc_info()[0]})')
        exit()'''