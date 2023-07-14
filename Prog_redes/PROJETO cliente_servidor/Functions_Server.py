from variables import *
import socket, sys

def PRINTS(x):
    print('-'*100)
    print(x)
    print('-'*100)
#----------------------------------------------------------------------------------------------------------
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

#----------------------------------------------------------------------------------------------------------
def broadCast(comunicacao, end_procurado, clients):
    comunicacao = f"{end_procurado} -> {comunicacao.decode(CODE)}"
    print (comunicacao)
    for conn, end in clients:
        if end != end_procurado:
            conn.send(comunicacao.encode(CODE))

#----------------------------------------------------------------------------------------------------------
def Client_Interaction(conn_server, end, clients):
    comunicacao = b''
    while comunicacao != b'/q':
        try:
            comunicacao = conn_server.recv(512)
            broadCast (comunicacao, end, clients)
        except:
            comunicacao = b'!q'
            clients.remove ((conn_server, end))
            conn_server.close()

#----------------------------------------------------------------------------------------------------------
def server_interaction(sock):
    msg = b' '
    while msg != b'':
        try:
            msg = sock.recv(512)
            print ("\n"+msg.decode(CODE)+"\n"+PROMPT)
        except:
            msg = b''
            print(f'Erro na decodificação do servidor... {sys.exc_info()[0]}')
def SPLIT(comunicacao):
    com_split = comunicacao.split(':')
    
def List_Clients(clients=None, sock=None, **kwargs):
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
def Whatsapp(comunicacao, clients):
    comunicacao = SPLIT(comunicacao)

def HELP(sock=None, **kwargs):
    try:
        # Criando descrição de cada comando
        descriptive_options = {
        '/l': 'Listar os clientes conectados',
        '/m:ip:porta:mensagem': 'Enviar mensagem para um cliente especifíco (informe IP:PORTA do cliente)',
        '/b:mensagem': 'Enviar mensagem em Broadcast (Para todos clientes conectados)',
        '/h': 'Lista o seu histórico de comandos',
        '/?': 'Lista as opções disponiveis',
        '/q': 'Desconectar do Servidor'
        }
        msg_title = f"\nSegue abaixo as Opções disponiveis neste servidor:"
        sock.send(msg_title.encode(CODE))
        for comando, descrição in descriptive_options.items(): # listando por meio do FOR comando por comando 
            msg_help = f"{comando} -> {descrição}\n" # formatação mensagem
            sock.send(msg_help.encode(CODE)) # enviando comando por comando
    except:
        print(f'\nErro no momento de listar as Opções...{sys.exc_info()[0]}')  
        exit()  
