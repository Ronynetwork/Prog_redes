HOST = 'localhost'
PORT = '50000'

import socket, sys, time
from constantes_tcp import *

try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    print('-'*100)
    print(f'\nSERVIDOR ATIVO: {server.getsockname()}')
    print('-'*100)
    server.listen()
    print('Aguardando a conexão do cliente...\n')
    print('-'*100);print('-'*100)
    conn, end = server.accept()
    print('Conexão aceita!')
except:
    print(f'Erro ao extabelecer conexão... {sys.exc_info()[0]}')
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
                conn.sendto(data_retorno, end)
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