from var import *
from Functions_and_Var import *
import socket, threading

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER_CLIENT, PORT))

    PRINTS (f'Conectado a: {SERVER_CLIENT, PORT}')
    tServer = threading.Thread(target=server_interaction, args=(sock,))
    tUser = threading.Thread(target=user_interaction,  args=(sock,))
    
    tServer.start()
    tUser.start()

    tServer.join()
    tUser.join()
    
except:
    print({sys.exc_info()})