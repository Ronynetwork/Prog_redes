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
    past = os.path.dirname(__file__) + '\\img_client\\'

    try: 
        os.path.exists(past)
        os.mkdir(past)

        PRINTS('O diretório img_client foi criado.')
    except:
        PRINTS('O diretório img_client já existe.\n\nContinuando a requisição...')

    return past

# Fechando a conexão caso o cliente solicite
        

def DADOS(dado_retorno):
    if 'Size:' in dado_retorno:
        tamanho_total = int(dado_retorno.split(':')[1])
        qtd_pacotes = math.ceil(tamanho_total/4096)
        return tamanho_total, qtd_pacotes
    
def PACOTES(client, arquivo, tamanho_total, qtd_pacotes):
    try:
        bytes_recebidos = 0
        pct = 1
        while True:
            dado_retorno = client.recv(4096)
            print(f'Pacote ({pct}/{qtd_pacotes}) - Dados Recebidos: {len(dado_retorno)} bytes')
            arquivo.write(dado_retorno)
            bytes_recebidos += len(dado_retorno)
            if bytes_recebidos >= tamanho_total:
                break
            pct += 1
    except:
        print(f'Erro ao baixar o arquivo... {sys.exc_info()[0]}')
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

def CHECAGEM(req):
    dir_atual = os.path.dirname(__file__)
    server_img = dir_atual + '\img_server\\'
    client_img = dir_atual + '\img_client\\'
    lista_arquivos = os.listdir(server_img)
    print(req)
    print()
    if req in lista_arquivos:
        arq_size = os.path.getsize(server_img + req)
        return (True, arq_size, server_img + req, client_img + req)
    else:
        arquivos_exist = []
        for x in lista_arquivos:
            if x.find(req) != -1:
                arquivos_exist.append(x)
        PRINTS(arquivos_exist)
        return (False,arquivos_exist)
    
