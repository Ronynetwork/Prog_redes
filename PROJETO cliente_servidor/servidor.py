''' IMPORTANDO BIBLIOTECAS NECESSÁRIAS PARA O FUNCIONAMENTO DO CÓDIGO '''
from Functions_and_Var import *

try:
    import threading, os, sys, logging, logging.config
except:
    print(f'\nErro na Importação das Bibliotecas necessárias...{sys.exc_info()[0]}')  
    sys.exit()

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
    PRINTS(f'\nErro na Inicialização da configuração do Log!


try:

    clients_list = {}
    while True:
        try:
            server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            server.bind((SERVER, PORT))
            ServerLog.info(f'\nServidor {SERVER} a espera de conexões na porta {PORT}!\n')
            server.listen()
            
            socket_client, client_info = server.accept()

            ServerLog.info (f'{client_info} Se conectou ao servidor.'); print('-'*100)
            clients_list[client_info[1]] = [client_info[0], socket_client] #Inserindo no dicionário a PORTA:IP do cliente
            tClient = threading.Thread(target=Client_Interaction, args=(socket_client, client_info, clients_list))

            tClient.start()
        except:
            ServerLog.critical(f'Erro na ao iniciar a Thread... {sys.exc_info()[0]}')
        
except OSError as e:
    ServerLog.critical ("Todas as portas do servidor estão ocupadas... ", e)

except SystemExit:
    print()

except:
    ServerLog.critical(f'Erro ao iniciar o Server... {sys.exc_info()[0]}')