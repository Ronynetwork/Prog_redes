from Functions_and_Var import *


try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((CLIENT, PORT))
    
    PRINTS (f'Conectado ao servidor: {SERVER}, na porta {PORT}')
    tServer = threading.Thread(target=server_interaction, args=(sock,))
    tUser = threading.Thread(target=user_interaction, args=(sock,))

    tServer.start()
    tUser.start()

    tServer.join()
    tUser.join()

except KeyboardInterrupt:
    print(f'\n\nVocê encerrou a conexão.\nVolte Sempre!\n')  
    exit()    

except: 
    print(f'Falha na conexão com o servidor... {sys.exc_info()[0]}')
    exit()