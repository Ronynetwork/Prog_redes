from Functions_and_Var import *
import socket, threading

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((SERVER, PORT))

    print ("Conectado a: ", (SERVER, PORT))
    tServer = threading.Thread(target=Server_Interaction)
    tUser = threading.Thread(target=Client_Interaction)

    tServer.start()
    tUser.start()

    tServer.join()
    tUser.join()

except Exception as e:
    print ('Erro... ', e)