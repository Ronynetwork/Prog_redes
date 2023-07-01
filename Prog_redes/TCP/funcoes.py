import socket, sys, os, math

def PRINTS(content):
    print('-'*100)
    print(content)
    print('-'*100)
    
def CONEXÃO_CLIENTE():
    try:    
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('localhost', 50000))
        print('\nConexão estabelecida!\n')
        return client
    except:
        print(f'Erro ao estabelecer a conexão com o servidor...{sys.exc_info()[0]}')

# Verificando se existe e criando a pasta img_client
def PAST_CLIENT():
    past = (os.path.dirname(os.path.abspath(__file__))) + '\\img_client\\'

    try: 
        os.path.exists(past)
        os.mkdir(past)

        PRINTS('O diretório img_client foi criado.')
    except:
        PRINTS('O diretório img_client já existe.\n\nContinuand a requisição...')

    return past

# Fechando a conexão caso o cliente solicite
        

def DADOS(dado_retorno):
    if 'Size:' in dado_retorno:
        tamanho_total = int(dado_retorno.split(':')[1])
        qtd_pacotes = math.ceil(tamanho_total/11264)
        return tamanho_total, qtd_pacotes
    
def PACOTES(client, arquivo, tamanho_total, qtd_pacotes):
    try:
        bytes_recebidos = 0
        pct = 1
        while True:
            dado_retorno = client.recv(11264)
            print(f'Pacote ({pct}/{qtd_pacotes}) - Dados Recebidos: {len(dado_retorno)} bytes')
            arquivo.write(dado_retorno)
            bytes_recebidos += len(dado_retorno)
            if bytes_recebidos >= tamanho_total: break
            pct += 1
    except:
        print(f'Erro ao baixar o arquivo... {sys.exc_info()}')
        arquivo.close()

# PARTE SERVIDOR

def CONEXÃO_SERVER():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', 50000))
        server.listen(1)

        PRINTS('\nAguardando a conexão com o cliente...\n')
        conn, end = server.accept()
        print(f'Conexão aceita!\n Cliente conectado {end}')

        print(f'\nSERVIDOR ATIVO: {server.getsockname()}')
        print('\nRecebendo Mensagens...\n\n')
        
        return conn, end, server
    except:
        print(f'Erro ao estabelecer a conexão... {sys.exc_info()[0]}')


def ENV_ARQ(conn, mensagem):
    try:
        # Nome do arquivo a ser enviado
        nome_arq = os.path.dirname(os.path.abspath(__file__)) + '\\img_server\\' + mensagem
        print(f'Enviando arquivo {mensagem} ...')

        tamanho_arquivo = os.path.getsize(nome_arq)
        msg = f'Size:{tamanho_arquivo}'
        conn.send(msg.encode('utf-8'))

        arquivo = open(nome_arq, 'rb')
        total_data_retorno = 0

        while True:
            data_retorno = arquivo.read(11264)
            total_data_retorno += len(data_retorno)
            conn.send(data_retorno)
            if not data_retorno:
                break

        print('-' * 100)
        print(f'\nArquivo {mensagem} Enviado...\n')
        print('-' * 100)

        arquivo.close()
    except:
        print(f'Erro ao eniviar o arquivo {sys.exc_info()[0]}')