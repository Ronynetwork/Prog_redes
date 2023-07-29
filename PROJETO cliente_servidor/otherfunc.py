import logging, logging.config, os, sys

# ============================================================================================================

''' DEFINIÇÃO DE ALGUMAS VARIAVEIS E DIRETÓRIOS '''

dir_atual = os.path.dirname(os.path.abspath(__file__))  # pegando a pasta atual
dir_arq =  os.path.abspath(__file__) 
dir_logconf = dir_atual + "\\log.ini"
dir_log = dir_atual + "\\serv_log.log"
dir_pastdownload = dir_atual + '\\server_files'

''' CONFIGURAÇÃO DO LOG '''

try:
    logging.config.fileConfig(dir_logconf, defaults={'log_path': dir_log.replace('\\', '\\\\')}) # lendo o log.ini na pasta atual
    urllib3_logger = logging.getLogger('urllib3') 
    urllib3_logger.setLevel(logging.WARNING) # deixando o level dos logs da URLLIB3 em warning (motivo: espama muitos logs info por conta das requisições do instagram)
    ServerLog  = logging.getLogger('Servidor') # pegando os logger definidos na configuração (Server/BotTelegram e debug para fins de debug do código)
    BotLog = logging.getLogger('TelegramBot')
    DebugLog = logging.getLogger('Debug')
except:
    PRINTS(f'\nErro na Inicialização da configuração do Log!\nVerifique se seu arquivo "log.ini" está configurado... {sys.exc_info()[0]}\n')
    sys.exit()