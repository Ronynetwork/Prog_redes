from Functions_and_Var import *
import socket, threading

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((CLIENT, PORT))

    PRINTS (f'Conectado a: " ({SERVER, PORT})')
    tServer = threading.Thread(target=server_interaction, args=(sock,))
    tUser = threading.Thread(target=user_interaction, args=(sock,))

    tServer.start()
    tUser.start()

    tServer.join()
    tUser.join()
    
except Exception as e:
    print ("Falha ", e)