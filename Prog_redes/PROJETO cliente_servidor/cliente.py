from constantes import *
import threading

try:
    print ("Conectado a: ", (SERVER, PORT))
    tServer = threading.Thread(target=server_interaction())
    tUser = threading.Thread(target=client_interaction())

    tServer.start()
    tUser.start()

    tServer.join()
    tUser.join()

except Exception as e:
    print ("Falha ", e)
