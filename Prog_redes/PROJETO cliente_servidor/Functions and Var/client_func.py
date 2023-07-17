from variables import *

#----------------------------------------------------------------------------------------------------------

'''                                        PARTE CLIENTE                                                '''

def client_interaction(sock):
    msg = ''
    while msg != '!q':
        try:
            msg = input(PROMPT)
            if msg != '': sock.send(msg.encode(CODE))
        except:
            msg = '!q'
    closeSocket(sock)

# ------------------------------------------------------------
def closeSocket(sock):
    try:
        sock.close()
    except:
        None

# ------------------------------------------------------------
def commands(msg, clients):
    while msg != '/q':
        if msg == '/l':
            print(clients)