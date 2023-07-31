import logging, logging.config, os, sys
from var import *

# ============================================================================================================
''' DEFINIÇÃO DE ALGUMAS VARIÁVEIS E DIRETÓRIOS '''

# Pegando o caminho absoluto do diretório atual do script
dir_atual = os.path.dirname(os.path.abspath(__file__))
# Pegando o caminho absoluto do próprio arquivo do script
dir_arq = os.path.abspath(__file__)
# Caminho para o arquivo de configuração de log 'log.ini' no diretório atual
dir_logconf = dir_atual + "\\log.ini"
# Caminho para o arquivo de log 'Server_Log.log'
dir_log = dir_atual + '\\Server_Log.log'
# Caminho para a pasta 'server_files' no diretório atual
dir_pastdownload = dir_atual + '\\server_files'

# ============================================================================================================
def PRINTS(x):
    '''Função para imprimir uma mensagem 'x' entre linhas de traços para melhor formatação no console.'''
    print('-'*100)
    print(x)
    print('-'*100)

# ============================================================================================================
''' CONFIGURAÇÃO DO LOG '''

try:
    # Configurando o log usando o arquivo 'log.ini' e definindo alguns loggers com nomes específicos
    logging.config.fileConfig(dir_logconf, defaults={'Log_server': dir_log.replace('\\', '\\\\')})
    # Obtendo o logger para o urllib3 e configurando para o nível de log WARNING
    urllib3_logger = logging.getLogger('urllib3') 
    urllib3_logger.setLevel(logging.WARNING)
    # Obtendo os loggers definidos na configuração (Servidor, TelegramBot e Debug)
    ServerLog = logging.getLogger('root')
    TeleLog = logging.getLogger('TelegramBot')
except:
    # Em caso de erro na configuração do log, imprime a mensagem de erro e encerra o programa
    PRINTS(f'\nErro na Inicialização da configuração do Log!\nVerifique se seu arquivo "log.ini" está configurado... {sys.exc_info()}\n')
    sys.exit()


# --------------------------------------------------------------------------------------------------------------------------------------------
def CREATE_PAST(name):
    '''Função para criar uma pasta com o nome fornecido como argumento.'''
    try:
        # Usando o 'os.makedirs' para criar a pasta com 'exist_ok=True' para evitar erros caso a pasta já exista
        os.makedirs(name, exist_ok=True)
    except:
        # Em caso de erro na criação da pasta, loga o erro usando o 'ServerLog' e encerra o programa
        ServerLog.error(f'Erro na Criação da Pasta...{sys.exc_info()[0]}')  
        exit() 

# ---------------------------------------------------------------------------------------------------------------------------------------------
def SPLIT_URL(url):
    '''Função para quebrar a URL e obter informações importantes.'''
    url_fragmentada = url.split('/')
    host = url_fragmentada[2] # Pegando o hostname (ex: freepik.com)
    local_arq = '/'+'/'.join(url_fragmentada[3:]) # Pegando o local do arquivo (ex: /image/ocean/iceocean.png)


# Continuando a partir da seção anterior...

    # Se houver um ponto (.) na última parte da URL, significa que há uma extensão de arquivo presente, então a removemos.
    if '.' in url_fragmentada[-1]:
        name_arq = url_fragmentada[-1].split('.')[0]  # Extrai o nome do arquivo sem a extensão.
    else:
        name_arq = url_fragmentada[-1]  # Se não houver extensão, usa a última parte da URL como o nome do arquivo.

    # Limita o tamanho máximo do nome do arquivo em 150 caracteres. Arquivos com nomes mais longos podem não ser salvos corretamente.
    if len(name_arq) >= 150:
        name_arq = name_arq[0:100]

    # Alguns caracteres não são permitidos em nomes de arquivos, então os removemos.
    caracteres_bloqueados = ['/', ':', '*', '?', '|', '<', '>', '"', '\\']
    for x in caracteres_bloqueados:
        name_arq = name_arq.replace(x, '')

    # Obtendo a parte do protocolo da URL (por exemplo, http, https, etc.).
    protocolo = url.split(':')[0]

    # Retorna o host, local_arq, name_arq e protocolo extraídos.
    return host, local_arq, name_arq, protocolo

# ----------------------------------------------------------------------------------------------------------------------------------------------
def SPLIT(x):
    '''Função para dividir uma string 'x' usando ':' como delimitador e retornar a lista resultante.'''
    try:
        comunicacao = x.split(':')
        return comunicacao
    except:
        # Em caso de erro durante a operação de divisão, registra o erro usando 'ServerLog'.
        ServerLog.error(f'Erro ao desmembrar a mensagem... {sys.exc_info()[0]}')

# ------------------------------------------------------------------------------------------------------------------------------------------------
def MSG_CLIENT(socket_client, comunicacao):
    '''Função para enviar uma mensagem 'comunicacao' para o cliente através do 'socket_client'.'''
    try:
        socket_client.send(comunicacao.encode(CODE))
    except:
        # Em caso de erro ao enviar a mensagem, registra o erro usando 'ServerLog'.
        ServerLog.error(f'Erro ao enviar mensagem para o cliente...{sys.exc_info()[0]}')
