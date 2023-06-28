import socket, sys

# Caso o arquivo sockets_constants.py esteja um diretório acima do atual
#diretorio_atual = os.path.dirname(os.path.abspath(__file__))
#diretorio_atual = diretorio_atual.rsplit('\\',1)[0]
#sys.path.insert(0, diretorio_atual)

from constantes_tcp import *

# Criando o socket UDP
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', PORT))
    try:
        while True:
            # Solicitar o arquivo
            nome_arquivo = input('Digite o nome do arquivo (EXIT p/ sair): ')
            
            # Enviando o nome do arquivo para o servidor
            print(f'\nSolicitando o arquivo {nome_arquivo}')
            client.send(nome_arquivo.encode(CODE_PAGE))
            print('-'*100)

            if nome_arquivo.upper() == 'EXIT': break

            dado_retorno = client.recv(BUFFER)
            dado_retorno = dado_retorno.decode(CODE_PAGE)
            if 'Size:' in dado_retorno:
                tamanho_total = int(dado_retorno.split(':')[1])

            # Gravar o dado recebido em arquivo
            print(f'Gravando o arquivo {nome_arquivo} ({tamanho_total} bytes)')
            try:
                nome_arquivo_ = DIR_ATUAL + '\\img_client\\' + nome_arquivo
                arquivo = open(nome_arquivo_, 'wb')
            except:
                print(f'Erro ao salvar o arquivo... {sys.exc_info()[0]}')
            bytes_recebidos = 0
            pct = 1
            while True:
                # Recebendo o conteúdo do servidor
                dado_retorno = client.recv(BUFFER)
                if not dado_retorno: break
                print(f'Pacote ({pct}) - Dados Recebidos: {len(dado_retorno)} bytes')
                arquivo.write(dado_retorno)
                bytes_recebidos += len(dado_retorno)
                if bytes_recebidos >= tamanho_total: break
                pct += 1
    except:
        print(f'Erro ao tentar estabelecer a conexão... {sys.exc_info()[0]}')

        arquivo.close()
except:
    print(f'Erro... {sys.exc_info()[0]}')
# Fechando o socket
client.close()
