import socket, os, sys

SERVER = '10.25.2.148'
PORT = 5678
PROMPT = 'Digite sua msg (!q para terminar) > '
CLIENT = 'localhost'
CODE = 'utf-8'

def PRINTS(x):
    print('-'*100)
    print(x)
    print('-'*100)

def conn_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', PORT))
        PRINTS('\nServidor a espera de conexões!\n')
        server.listen(6)

        return server

    except:
        print(f'Erro ao estabaelecer a conexão do servidor{sys.exc_info()}')

    
def broadCast(comunicacao, end_procurado, clients):
    comunicacao = f"{end_procurado} -> {comunicacao.decode(CODE)}"
    print (comunicacao)
    for conn, end in clients:
        if end != end_procurado:
            conn.send(comunicacao.encode(CODE))

def Client_Interaction(conn_server, end, clients):
    command = b''
    while command != b'!q':
        try:
            command = conn_server.recv(512)
            broadCast (command, end)
        except:
            command = b'!q'
            clients.remove ((conn_server, end))
            conn_server.close()

#----------------------------------------------------------------------------------------------------------

'''                                        PARTE CLIENTE                                                '''

def server_interaction(sock):
    msg = b' '
    while msg != b'':
        try:
            msg = sock.recv(512)
            print ("\n"+msg.decode(CODE)+"\n"+PROMPT)
        except:
            msg = b''
    closeSocket()

def client_interaction(sock):
    msg = ''
    while msg != '!q':
        try:
            msg = input(PROMPT)
            if msg != '': sock.send(msg.encode(CODE))
        except:
            msg = '!q'
    closeSocket()

def closeSocket(sock):
    try:
        sock.close()
    except:
        None