''' IMPORTANDO BIBLIOTECAS NECESSÁRIAS PARA O FUNCIONAMENTO DO CÓDIGO '''
from otherfunc import *
from Functions_and_Var import *
from telegram import *
import threading


try:
    clients_list = {}
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((SERVER, PORT))
    server.listen()
    
    ServerLog.info(f'Servidor {SERVER} a espera de conexões na porta {PORT}!')
    PRINTS(f'Servidor {SERVER} a espera de conexões na porta {PORT}!')
    bot_thread = threading.Thread(target=Run_bot, args= (clients_list, dir_log))
    bot_thread.start()
    CREATE_PAST(dir_atual + '\\server_files')
    
    try:
        while True:
            socket_client, client_info = server.accept()
            ServerLog.info (f'{client_info} Se conectou ao servidor.')
            clients_list[client_info[1]] = [client_info[0], socket_client] #Inserindo no dicionário a PORTA:IP do cliente
            tClient = threading.Thread(target=Client_Interaction, args=(socket_client, client_info, clients_list))

            tClient.start()
    except:
        ServerLog.error(f'Erro na ao iniciar a Thread... {sys.exc_info()[0]}')
        
except OSError as e:
    ServerLog.error ("Todas as portas do servidor estão ocupadas... ", e)

except SystemExit:
    ServerLog.debug('Alguma área do código executou a função exit().')

except:
    ServerLog.error(f'Erro ao iniciar o Server... {sys.exc_info()[0]}')