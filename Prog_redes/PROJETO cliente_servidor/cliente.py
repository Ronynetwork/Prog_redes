from Functions_and_Var import *
import threading

try:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((CLIENT, PORT))
    print ("Conectado a: ", (CLIENT, PORT))
    tServer = threading.Thread(target=server_interaction, args=(sock,))
    tUser = threading.Thread(target=client_interaction, args=(sock,))

    tServer.start()
    tUser.start()

    tServer.join()
    tUser.join()

except Exception as e:
    print ("Falha ", e)