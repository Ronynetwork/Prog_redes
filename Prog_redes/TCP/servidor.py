import socket, sys, os, time

# Caso o arquivo sockets_constants.py esteja um diretório acima do atual
#diretorio_atual = os.path.dirname(os.path.abspath(__file__))
#diretorio_atual = diretorio_atual.rsplit('\\',1)[0]
#sys.path.insert(0, diretorio_atual)

from constantes_tcp import *

endereço = (('localhost', PORT))
# Criando o socket UDP
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(endereço) 
    server.listen(1)
    print('Aguardando a conexão do cliente...\n')
    print('-'*100)
    conn, end = server.accept()
    print(f'Conexão aceita!\n Cliente conectado {end}')
except:
    print(f'Erro de conexão...')
# Vincular o socket a tupla (host, port)

print(f'\nSERVIDOR ATIVO: {server.getsockname()}')
print('\nRecebendo Mensagens...\n\n')

try:
    while True:
        mensagem = conn.recv(BUFFER)
        mensagem = mensagem.decode(CODE_PAGE)
        if mensagem.upper() == 'EXIT':
            print(f'\nO {end} SE DESCONECTOU DO SERVIDOR...\n')
        else:
            # Nome do arquivo a ser enviado
            nome_arquivo = DIR_ATUAL + '\\img_server\\' + mensagem
            print(f'Enviando arquivo {mensagem.upper()} ...')

            tamanho_arquivo = os.path.getsize(nome_arquivo)
            msg = f'Size:{tamanho_arquivo}'.encode(CODE_PAGE)
            conn.send(msg)

            arquivo = open(nome_arquivo, 'rb')
            while True:
                data_retorno = arquivo.read(BUFFER)
                if not data_retorno: break                                
                conn.send(data_retorno)
                time.sleep(0.02)
            print(f'Arquivo {mensagem.upper()} Enviado...')
            arquivo.close()
except KeyboardInterrupt:
    print('Foi pressionado CTRL+C')
    # Fechando o socket
    server.close()    
except:
    print(f'\nERRO: {sys.exc_info()[0]}')
finally:    
    # Fechando o socket
    server.close()