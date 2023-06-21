import socket, sys, os, time
from server_constantes import *

atual_dir = os.path.dirname(os.path.abspath(__file__)) 

# Criando o socket UDP
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Vincular o socket a tupla (host, port)
udp_socket.bind((HOST_SERVER, SOCKET_PORT)) 

print(f'\nSERVIDOR ATIVO: {udp_socket.getsockname()}')
print('\nRecebendo Mensagens...\n\n')

try:
    while True:
        mensagem, ip_cliente = udp_socket.recvfrom(BUFFER_SIZE)
        mensagem = mensagem.decode(CODE_PAGE)
        if mensagem.upper() == 'EXIT':
            print(f'\nO {ip_cliente} SE DESCONECTOU DO SERVIDOR...\n')
        else:
            # Nome do arquivo a ser enviado
            nome_arquivo = atual_dir + '\\img\\' + mensagem
            print(f'Enviando arquivo {mensagem.upper()} ')  

            tamanho_arquivo = os.path.getsize(nome_arquivo)
            msg = f'Size:{tamanho_arquivo}'.encode(CODE_PAGE)
            udp_socket.sendto(msg, ip_cliente)

            arquivo = open(nome_arquivo, 'rb')# Lendo em binário a mensagem
            while True:
                data_retorno = arquivo.read(BUFFER_SIZE)
                if not data_retorno: break                                
                udp_socket.sendto(data_retorno, ip_cliente)
                time.sleep(0.02)
            print(f'Arquivo {mensagem.upper()} Enviado...')
            arquivo.close()

except KeyboardInterrupt:
    print('Foi pressionado CTRL+C')
    # Fechando o socket
    udp_socket.close()    
except:
    print(f'\nERRO: {sys.exc_info()[0]}')
finally:    
    # Fechando o socket
    udp_socket.close()