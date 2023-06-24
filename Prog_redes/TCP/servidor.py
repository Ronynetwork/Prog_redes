import socket, sys, time
from constantes_tcp import *

try:
    endereço_server = ('localhost',PORT)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(endereço_server)
    print('-'*100)
except:
    print(f'Erro ao estabelecer conexão...{sys.exc_info()[0]}')
server.listen(1)
time.sleep(5)
print('Aguardando a conexão do cliente...\n')
print('-'*100)
conn, end = server.accept()
print(f'Conexão aceita!\n Cliente conectado {end}')

try:
    while True:
        req_client = conn.recv(BUFFER)
        req_client = req_client.decode(CODE_PAGE)

        if req_client.upper() == 'EXIT':
            print(f'\nO {end} SE DESCONECTOU DO SERVIDOR...\n')
            conn.close()

        else:
            # Nome do arquivo a ser enviado
            nome_arquivo = DIR_ATUAL + '\\img\\' + req_client.lower()

            print(f'Enviando arquivo {req_client} ')  
            tamanho_arquivo = os.path.getsize(nome_arquivo)     

            msg = f'Size:{tamanho_arquivo}'.encode(CODE_PAGE)
            conn.sendto(msg, end)

            arquivo = open(nome_arquivo, 'rb')# Lendo em binário a mensagem
            while True:
                data_retorno = arquivo.read(BUFFER)

                if not data_retorno: break                                
                conn.sendall(data_retorno, end)
                time.sleep(0.02)

            print(f'Arquivo {req_client.upper()} Enviado...')
            arquivo.close()

except KeyboardInterrupt:
    print('Foi pressionado CTRL+C')
    server.close()    
except:
    print(f'\nERRO: {sys.exc_info()[0]}')
finally:    
    # Fechando o socket
    conn.close()
    server.close()