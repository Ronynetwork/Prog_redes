import os, sys

MAX_NOT = 15
MSG_SIZE = 512
SERVER_CLIENT = 'localhost'
SERVER = '0.0.0.0'
PORT = 5678
PROMPT = 'Digite sua mensagem ->  '
CODE = 'utf-8'
BUFFER = 4096


def PRINTS(x):
    print('-'*100)
    print(x)
    print('-'*100)

# ---------------------------------------------------------------------------------------------------------------------------------------------
def SPLIT_URL (url): # FUNÇÃO PARA QUEBRAR A URL E PEGAR INFORMAÇÕES IMPORTANTES
    url_fragmentada = url.split('/')
    host = url_fragmentada[2] # pegando o hostname (ex: freepik.com)
    local_arq = '/'+'/'.join(url_fragmentada[3:]) # pegando local do arquivo (ex: /image/ocean/iceocean.png)
    if '.' in url_fragmentada[-1]: # isso é para retirar a extensão que tiver anteriormente [Há qual as vezes não é a mesma contida no content-type]
        name_arq = url_fragmentada[-1].split('.')[0]
    else:
        name_arq = url_fragmentada[-1]
    if len(name_arq) >= 150: # mantendo o máximo do tamanho do arquivo em 150 caracteres [Ultrapassando esse valor ele não irá salvar o arquivo corretamente]
        name_arq = name_arq[0:100]
    caracteres_bloqueados = ['/', ':', '*', '?', '|', '<', '>', '"', '\\'] 
    for x in caracteres_bloqueados: # retirando caracteres que são proibidos de ter no nome de um arquivo, para salvar...
        name_arq = name_arq.replace(x, '') 
    protocolo = url.split(':')[0] # pegando o protocolo da url
    return host, local_arq, name_arq, protocolo

# ----------------------------------------------------------------------------------------------------------------------------------------------
def SPLIT(x):
    try:
        comunicacao = x.split(':')
        return comunicacao
    except:
        print(f'Erro ao desmembrar a mensagem... {sys.exc_info()[0]}')

# ------------------------------------------------------------------------------------------------------------------------------------------------
def MSG_CLIENT(socket_client, comunicacao):
    try:
        socket_client.send(comunicacao.encode(CODE))
    except:
        loggerServer.error(f'Erro ao enviar mensagem para o cliente...{sys.exc_info()[0]}')