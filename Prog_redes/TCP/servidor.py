import socket, sys, os, time

# Caso o arquivo sockets_constants.py esteja um diretório acima do atual
#diretorio_atual = os.path.dirname(os.path.abspath(__file__))
#diretorio_atual = diretorio_atual.rsplit('\\',1)[0]
#sys.path.insert(0, diretorio_atual)

from constantes_tcp import *

endereço = (('localhost', PORT))
# Criando o socket UDP
try:
    # Abrindo a conexão TCP com o cliente
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(endereço) # Associando o socket de servidor a um endereço
    server.listen(1) # Escutando para tentar detecar uma conexão

    print('-'*100)
    print('\nAguardando a conexão do cliente...\n')
    print('-'*100)
        
    conn, end = server.accept() 
    print(f'Conexão aceita!\n Cliente conectado {end}')
    # Vincular o socket a tupla (host, port)

    print(f'\nSERVIDOR ATIVO: {server.getsockname()}')
    print('\nRecebendo Mensagens...\n\n')

    while True:
        mensagem = (conn.recv(11264).decode('utf-8'))

        if mensagem.lower() == 'exit':
            print(f'\nO {end} SE DESCONECTOU DO SERVIDOR...\n')
            break
        # Nome do arquivo a ser enviado
        name_arq = DIR_ATUAL + '\\img_server\\' + mensagem
        print(f'Enviando arquivo {mensagem} ...')

        tamanho_arquivo = os.path.getsize(name_arq)
        msg = f'Size:{tamanho_arquivo}'
        conn.send(msg.encode('utf-8'))
        
        arquivo = open(name_arq, 'rb')
        total_data_retorno = 0
        while True:
            data_retorno = arquivo.read(11264)
            total_data_retorno += len(data_retorno)
            conn.send(data_retorno)
            if not data_retorno: break                                
            time.sleep(0.02)

        print('-'*100)
        print(f'\nArquivo {mensagem} Enviado...\n')
        print('-'*100)

        arquivo.close()
except FileNotFoundError:
    conn.send('O arquivo não existe em nossa base de dados')
    while True:
        data_retorno = arquivo.read(11264)
        total_data_retorno += len(data_retorno)
        conn.send(data_retorno)
        if not data_retorno: break                                
except:
    print(f'\nERRO: {sys.exc_info()[0]}')
finally:
    conn.close()
    server.close()