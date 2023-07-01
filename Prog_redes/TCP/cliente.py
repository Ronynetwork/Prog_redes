import socket, sys, time, math

# Caso o arquivo sockets_constants.py esteja um diretório acima do atual
#diretorio_atual = os.path.dirname(os.path.abspath(__file__))
#diretorio_atual = diretorio_atual.rsplit('\\',1)[0]
#sys.path.insert(0, diretorio_atual)

from constantes_tcp import *

# Criando o socket UDP
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', PORT))
    print('\nConexão estabelecida!\n')
    time.sleep(1)
    past = DIR_ATUAL + '\\img_client\\'

    try:
        os.path.exists(past)
        os.makedirs(past)

        print('-'*100)
        print(f'O diretório img_client foi criado.')
        print('-'*100)
        
    except:
        print('-'*100)
        print(f'O diretório img_client já existe.\n\nCotinuando a requisição...')
        print('-'*100)
    try:
        while True:
            # Solicitar o arquivo
            nome_arquivo = input('Digite o nome do arquivo (EXIT p/ sair):');print('-'*100)

            if nome_arquivo.lower() == 'exit': 
                client.send(nome_arquivo)
                print('Você solicitou o fim da conexão.\n\nAté a próxima!!')
                print('-'*100)
                break         

            # Enviando o nome do arquivo para o servidor
            client.send(nome_arquivo.encode('utf-8'))

            print(f'\nSolicitando o arquivo {nome_arquivo}')
            print('-'*100)

            dado_retorno = (client.recv(11264)).decode('utf-8')

            
            if 'Size:' in dado_retorno:
                tamanho_total = int(dado_retorno.split(':')[1])
                print(tamanho_total)
                qtd_pacotes = math.ceil(tamanho_total/11264)
                
            # Gravar o dado recebido em arquivo
            print(f'Gravando o arquivo {nome_arquivo} ({tamanho_total} bytes)')
            try:
                nome_arquivo = past + nome_arquivo
                arquivo = open(nome_arquivo, 'wb')
            except:
                print(f'Erro ao salvar o arquivo... {sys.exc_info()[0]}')
            bytes_recebidos = 0
            pct = 1
            while True:
                # Recebendo o conteúdo do servidor
                dado_retorno = client.recv(11264)

                if not dado_retorno: break

                print(f'Pacote ({pct}/{qtd_pacotes}) - Dados Recebidos: {len(dado_retorno)} bytes')
                arquivo.write(dado_retorno)
                bytes_recebidos += len(dado_retorno)
                if bytes_recebidos >= tamanho_total: break
                pct += 1
    except:
        print(f'Erro ao baixar o arquivo... {sys.exc_info()[0]}')
        arquivo.close()
except:
    print(f'Erro... {sys.exc_info()[0]}')
# Fechando o socket
client.close()
