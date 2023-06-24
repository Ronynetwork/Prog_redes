import socket, sys, os, time
from socket_constants import *

# Criando o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # Definindo uma conexão UDP e de IPv4
# Vincular o socket a tupla (host, port)
udp_socket.bind((HOST_SERVER, SOCKET_PORT)) 
print(f'\nSERVIDOR ATIVO: {udp_socket.getsockname()}')
print('\nRecebendo Mensagens...\n\n')
try:
    while True:
        req_client, ip_cliente = udp_socket.recvfrom(BUFFER_SIZE)
        req_client = req_client.decode(CODE_PAGE)

        if req_client.upper() == 'EXIT':
            print(f'\nO {ip_cliente} SE DESCONECTOU DO SERVIDOR...\n')
            udp_socket.close()

        else:
            # Nome do arquivo a ser enviado
            nome_arquivo = DIR_ATUAL + '\\img\\' + req_client.lower()

            print(f'Enviando arquivo {req_client} ')  
            tamanho_arquivo = os.path.getsize(nome_arquivo)     

            msg = f'Size:{tamanho_arquivo}'.encode(CODE_PAGE)
            udp_socket.sendto(msg, ip_cliente)

        with open(nome_arquivo, 'rb') as arquivo:
            
            while True:
                data_retorno = arquivo.read(BUFFER_SIZE)

                if not data_retorno: break                                
                udp_socket.sendto(data_retorno, ip_cliente)
                time.sleep(0.02)

            print(f'Arquivo {req_client.upper()} Enviado...')
            arquivo.close()

except KeyboardInterrupt:
    print('Foi pressionado CTRL+C')
    udp_socket.close()    
except:
    print(f'\nERRO: {sys.exc_info()[0]}')
finally:    
    # Fechando o socket
    udp_socket.close()