import socket, sys

SERVER = '0.0.0.0'
PORT = 5678
PROMPT = 'Digite sua msg (!q para terminar) > '
CLIENT = 'localhost'
CODE = 'utf-8'

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
    closeSocket(sock)

def SPLIT(msg):
    comunica
#----------------------------------------------------------------------------------------------------------

'''                                        PARTE CLIENTE                                                '''

def client_interaction(sock):
    msg = ''
    while msg != '!q':
        try:
            msg = input(PROMPT)
            if msg != '': sock.send(msg.encode(CODE))
        except:
            msg = '!q'
    closeSocket(sock)

# ------------------------------------------------------------
def closeSocket(sock):
    try:
        sock.close()
    except:
        None

# ------------------------------------------------------------
def commands(msg, clients):
    while msg != '/q':
        if msg == '/l':
            print(clients)