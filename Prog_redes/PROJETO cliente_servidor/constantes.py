import socket, os, sys

def PRINTS(x):
    print('-'*100)
    print(x)
    print('-'*100)

def connm_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', 50000))
        server.listen(6)

        PRINTS('\nAguardando a conexão com o cliente...\n')
        conn, end = server.accept()
        print(f'Conexão aceita!\n Cliente conectado {end}')

        print(f'\nSERVIDOR ATIVO: {server.getsockname()}')
        print('\nRecebendo Mensagens...\n\n')
        
    except:
        print(f'Erro ao estabaelecer a conexão do servidor{sys.exc_info()}')
        return server, conn, end
    
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
    
    def 