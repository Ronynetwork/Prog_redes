import socket, sys

SERVER = '10.25.2.148'
CLIENT = 'localhost'
PORT = 5678
PROMPT = 'Digite sua msg (!q para terminar) > '
CODE = CODE

def PRINTS(x):
    print('-'*100)
    print(x)
    print('-'*100)

def conn_server():
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('localhost', PORT))
        sock.listen(6)

        print(f'\nSERVIDOR ATIVO: {sock.getsockname()}')
        print('\nRecebendo Mensagens...\n\n')
        
    except:
        print(f'Erro ao estabaelecer a conexão do servidor{sys.exc_info()}')
        return sock
    
def Client_Interaction(conn_server, end,clients):
    command = b''
    while command != b'!q':
        try:
            command = conn_server.recv(512)
            broadCast (command, end)
        except:
            command = b'!q'
            clients.remove ((conn_server, end))
            conn_server.close()
def Server_Interaction(sock):
    msg = b' '
    while msg != b'':
        try:
            msg = sock.recv(512)
            print ("\n"+msg.decode(CODE)+"\n"+PROMPT)
        except:
            msg = b''
    closeSocket()

def closeSocket(sock):
    try:
        sock.close()
    except:
        None

def broadCast(msg, addrSource,clients):
    msg = f"{addrSource} -> {msg.decode(CODE)}"
    print (msg)
    for sockConn, addr in clients:
        if addr != addrSource:
            sockConn.send(msg.encode(CODE))
    