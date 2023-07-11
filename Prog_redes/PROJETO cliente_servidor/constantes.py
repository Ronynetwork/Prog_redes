import socket, os, sys

def PRINTS(x):
    print('-'*100)
    print(x)
    print('-'*100)

def conn_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', 50000))
        server.listen(6)
        
    except:
        print(f'Erro ao estabaelecer a conexão do servidor{sys.exc_info()}')

        return server
    
def broadCast(comunicacao, end_procurado, clients):
    comunicacao = f"{end_procurado} -> {comunicacao.decode('utf-8')}"
    print (comunicacao)
    for conn, end in clients:
        if end != end_procurado:
            conn.send(comunicacao.encode('utf-8'))

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