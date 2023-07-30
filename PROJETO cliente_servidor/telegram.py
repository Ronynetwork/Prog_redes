from otherfunc import *
import requests, time

# ============================================================================================================
API = '6338998807:AAGvV1OnJRlG24Bu5Au0n1N4HXnMg1KCWj8'
url_req = f'https://api.telegram.org/bot{API}' # montagem variavel para requisição
id_chat = 5506756754 # PREENCHA AQUI COM O ID CHAT DO SEU BOT

# ============================================================================================================

''' FAZENDO A VALIDAÇÃO DA API_KEY '''

def VERIFICATION_KEY(): 
    try:
        key_verify = requests.get(url_req + '/getUpdates').json() # realizando uma requisição
    except:
        print(f'\nErro na Verificação da API_KEY...{sys.exc_info()[0]}')  
        sys.exit()
    else:
        if key_verify.get('ok'): # verificando se a requisição foi completa
            TeleLog.info(f'Sua API foi verificada com sucesso!')  
            pass # se true, continua o código
        else:
            print(f'\nA chave: {API}\nInformada é inválida!')
            sys.exit()
   
VERIFICATION_KEY()

# ============================================================================================================

''' FUNÇÃO PARA NOTIFICAR O BOT A CADA CLIENTE CONECTADO '''

def Bot_notification(msg_connected):
    try:
        resposta = {'chat_id':id_chat,'text':f'{msg_connected}'} # realizo a montagem da formatação para o chat com id especificado
        var = requests.post(url_req+'/sendMessage',data=resposta) # envio a mensagem via requests.post
    except:
        TeleLog.error(f'Erro no envio da mensagem de [Cliente Conectado] para o Bot...{sys.exc_info()[0]}')  
        sys.exit()

# ============================================================================================================

''' FUNÇÃO PARA LISTAR OS CLIENTES CONECTADOS AO BOT '''

def Bots_clients(connect_clients):
    try:
        num = 0
        if len(connect_clients) > 0: # verifica se existe algum cliente conectado
            msg_list = "Os clientes conectados são:\n" # formatação mensagem
            for chave, valor in connect_clients.items(): # pego cada cliente conectado (ip/porta) do dicionário já criado
                num+=1 # formatação numeração cliente
                msg_list += f"\nCLIENTE {num}\nIP: {valor[0]}\nPORTA: {chave}\n\n" # formatação listagem clientes (lembrando que chave=porta e valor[0]=ip
        else: # se não existir ele informa para o chat que não possui nenhum conectado
            msg_list = "O Servidor não possui nenhum cliente conectado!"
        resposta = {'chat_id':id_chat,'text':f'{msg_list}'} # realizo a montagem da formatação para o chat com id especificado
        var = requests.post(url_req+'/sendMessage',data=resposta) # envio a mensagem via requests.post
    except:
        TeleLog.error(f'Erro no momento de Listar os Clientes Conectados...{sys.exc_info()[0]}')  
        sys.exit() 

# ============================================================================================================

''' LISTANDO O LOG PARA O BOT DO TELEGRAM '''

def Log_bot(dir_log):
    try:
        file_name = 'log-server.txt'
        with open(dir_log, 'rb') as arquive: 
            log = arquive.read()    
        send_mesage = requests.post(url_req+'/sendDocument', data={'chat_id': id_chat}, files={'document': (file_name, log)}) # realizo envio do Log como documento
    except:
        TeleLog.error(f'Erro no momento de listar o Log para o Bot do Telegram...{sys.exc_info()}')  
        sys.exit() 

# ============================================================================================================

''' INFORMANDO PARA DIGITAR UM COMANDO VÁLIDO '''

def INVALID():
    try:
        msg_invalid = "\nInforme um comando válido!\n\n/u -> Listagem de Clientes Conectados\n/log -> Listagem do Log atual do servidor\n"
        msg_invalid += "\nBy: https://github.com/kakanetwork"
        resposta = {'chat_id':id_chat,'text':f'{msg_invalid}'} # faço o envio
        var = requests.post(url_req+'/sendMessage',data=resposta) 
    except:
        TeleLog.error(f'Erro no momento de Informar para digitar um comando válido...{sys.exc_info()[0]}')  
        sys.exit() 

# ============================================================================================================

''' FUNÇÃO PARA RECEBER MENSAGENS/COMANDOS DA CONVERSA COM O BOT '''

def Run_bot(clients_connected, dir_log):
    try:
        message_ID = None # defino o id da mensagem como NONE, usado mais a frente
        while True: # while True para ficar "ouvindo" o chat
            # faço o get com o parametro offset = id_message, que inicialmente é NONE, transformo em .json e pego apenas oque tem dentro da variavel "RESULT"
            # isso me retorna todas as últimas mensagens do chat e seus parametros (ex: id da mensagem, pelo ID eu consigo identificar a última mensagem)
            chat = requests.get(url_req + '/getUpdates', params={'offset': message_ID}).json().get('result', [])
            num_chat = len(chat)
            if num_chat == 0: # verificando se o chat tá vazio, se estiver ele dá sleep de 1s, e volta pro while para não gastar processamento extra
                time.sleep(0.5)
                continue
            for msg in chat: # pego cada mensagem das últimas mensagens
                if 'message' in msg and 'text' in msg['message']: # verifico se a chave 'message' e 'text' estão presentes
                    command = msg['message']['text'] # pego o texto da mensagem
                    if command == '/u' : # verifico se o que foi digitado = /u
                        TeleLog.info('Foi pedido para Listar os Clientes Conectados!')
                        Bots_clients(clients_connected) # se sim, ativo a função de listagem dos clientes conectados
                    elif command == '/log':
                        TeleLog.info('Foi pedido para Listar o Log Atual!')
                        Log_bot(dir_log) # se sim, ativo a função de listagem do log
                    else:
                        msg_invalid = "\ncomando inválido! segue os comandos aceitos:\n\n/u -> Lista de Clientes Conectados\n/log -> Lista do Log atual do servidor\n"
                        msg_invalid += "\nPor: https://github.com/Ronynetwork"
                        resposta = {'chat_id':id_chat,'text':f'{msg_invalid}'} # faço o envio
                        var = requests.post(url_req+'/sendMessage',data=resposta)
                message_ID= msg['update_id'] + 1 # aqui eu defino o id message (pego ele dentro do .json), e jogo +1 pois funciona como um OFFSET
                # onde a cada mensagem, o seu id vai ser +1 em relação ao anterior
    except:
        TeleLog.error(f'Erro no momento de Ler as mensagens do Telegram...{sys.exc_info()}')  
        sys.exit() 

# ============================================================================================================
