import logging, logging.config, os, sys
from var import *


# ============================================================================================================

''' DEFINIÇÃO DE ALGUMAS VARIAVEIS E DIRETÓRIOS '''

dir_atual = os.path.dirname(os.path.abspath(__file__))  # pegando a pasta atual
dir_arq =  os.path.abspath(__file__) 
dir_logconf = dir_atual + "\\log.ini"
dir_log = dir_atual + '\\Server_Log.log'
dir_pastdownload = dir_atual + '\\server_files'


def PRINTS(x):
    print('-'*100)
    print(x)
    print('-'*100)

''' CONFIGURAÇÃO DO LOG '''

try:
    logging.config.fileConfig(dir_logconf, defaults={'Log_server': dir_log.replace('\\', '\\\\')}) # lendo o log.ini na pasta atual
    urllib3_logger = logging.getLogger('urllib3') 
    urllib3_logger.setLevel(logging.WARNING) # deixando o level dos logs da URLLIB3 em warning (motivo: espama muitos logs info por conta das requisições do instagram)
    ServerLog  = logging.getLogger('Servidor') # pegando os logger definidos na configuração (Server/BotTelegram e debug para fins de debug do código)
    TeleLog = logging.getLogger('TelegramBot')
    DebugLog = logging.getLogger('Debug')
except:
    PRINTS(f'\nErro na Inicialização da configuração do Log!\nVerifique se seu arquivo "log.ini" está configurado... {sys.exc_info()}\n')
    sys.exit()

# --------------------------------------------------------------------------------------------------------------------------------------------
def CREATE_PAST(name):
    try:
        os.makedirs(name, exist_ok=True) # utilizando makedirs para ter o parametro "exist_ok=true" para caso a pasta exista, não retorne erro!
    except:
        ServerLog.error(f'Erro na Criação da Pasta...{sys.exc_info()[0]}')  
        exit()      

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
        ServerLog.error(f'Erro ao desmembrar a mensagem... {sys.exc_info()[0]}')

# ------------------------------------------------------------------------------------------------------------------------------------------------
def MSG_CLIENT(socket_client, comunicacao):
    try:
        socket_client.send(comunicacao.encode(CODE))
    except:
        ServerLog.error(f'Erro ao enviar mensagem para o cliente...{sys.exc_info()[0]}')