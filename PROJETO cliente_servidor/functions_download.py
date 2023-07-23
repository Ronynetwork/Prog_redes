import sys, socket, os, ssl, socket
#                                          VARIÁVEIS                                                   <:

SERVER = '0.0.0.0'
PORT = 5678
PROMPT = 'Digite sua msg (/q para terminar) > '
CLIENT = 'localhost'
CODE = 'utf-8'
BUFFER = 512

# ---------------------------------------------------------------------------------------------------------------------------------------------------
def SOCKET_HTTPS(localarquive, hostname):
    req = f'GET {localarquive} HTTP/1.1\r\nHOST: {hostname}\r\nConnection: close\r\n\r\n'    # define a requisição 
    context = ssl.create_default_context()      # criação do contexto SSL para conexão HTTPS
    context.check_hostname = False      # desativa a verificação do nome do host durante a autenticação SSL.
    context.verify_mode = ssl.CERT_NONE     # o certificado do servidor não será verificado
    socket_TCP_IPV4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # criação do socket/ conexão com o server (IPV4/TCP)
    socket_conexão = context.wrap_socket(socket_TCP_IPV4, server_hostname=hostname)     # Envolve o socket criado anteriormente em uma conexão segura (wrap_socket)
    socket_conexão.connect((hostname, 443))     # estabelece a conexão
    socket_conexão.send(req.encode(CODE))     # enviando requisição pedida acima
    return socket_conexão # retornando conexão 


# ---------------------------------------------------------------------------------------------------------------------------------------------------

def SOCKET_HTTP(localarquive, hostname):
    requisição = f'GET {localarquive} HTTP/1.1\r\nHOST: {hostname}\r\nConnection: close\r\n\r\n'
    socket_conexão = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_conexão.connect((hostname, 80))
    socket_conexão.sendall(requisição.encode(CODE))
    return socket_conexão

# ============================================================================================================

def CONT_LEN(header):
    try:
        lines = header.strip().split('\n')  # pego o header já decodificado e quebro ele em linhas
        for line in lines:
            if line.lower().startswith('content-length:'): # vasculho nessas linhas o content-length por meio do startswich que retorna True quando a palavra existir
                lenght = int(line[16:]) # transforma em int e pega somente da posição 16 em diante
                return lenght 
    except:
        print(f'\nErro na captura do Content-Type...{sys.exc_info()[0]}')
def CONT_TYPE(header):
    try:
        lines = header.strip().split('\n')
        for line in lines:
            extension = line.strip().split('/')[1]
            return extension
    except:
        print(f'Erro ao localizar o content-type. {sys.exc_info()[0]}')
            
def DOWNLOAD_WEB(socket_conexão, sock_client):
    data_ret = b'' 
    dados_recebidos = 0
    try:
        content_lenght = -1
        msg_download = f'\nDownload do Arquivo foi Iniciado!\n'
        
        sock_client.send(msg_download.encode(CODE))

        while True:     # recebendo a resposta 
            data = socket_conexão.recv(BUFFER)    # recebe a resposta em pedaços de Xbytes (x = buffer_size)
            if not data: 
                break
            data_ret += data
            dados_recebidos += len(data)    # joga na variavel o quanto de bytes já foram recebidos
            position  = data_ret.find('\r\n\r\n'.encode())
            header   = data_ret[:position].decode('utf-8').lower()   # pegando o cabeçalho 
            try:
                content_lenght = CONT_LEN(header)    # função para capturar o content length no header
                msg_download = f'\rBytes baixados: {dados_recebidos} / {content_lenght} bytes'
                sock_client.send(msg_download.encode(CODE))
            except: pass  # passando pois o content_lenght não é vital para o código
        if content_lenght == -1:
            msg_size = 'Não foi possivel capturar o Content_Lenght...'
            sock_client.send(msg_size.encode(CODE)) # criando um aviso para quando o content lenght não for pego 
        arquivo_dados = data_ret[position+4:]   # pegando os dados do arquivo
        content_type = CONT_TYPE(header) # usando a função para pegar a extensão do arquivo pelo header
        msg_download = f'\nO Download do arquivo foi concluído!\n'
        try:
            socket_conexão.send(msg_download.encode(CODE))
        except:
            print(f'\nErro ao enviar mensagem para o cliente...{sys.exc_info()[0]}')
    except:
        print(f'\nErro no recebimento dos dados...{sys.exc_info()}')  
        exit()  
    socket_conexão.close() # fechando a conexão
    return header, arquivo_dados, content_type