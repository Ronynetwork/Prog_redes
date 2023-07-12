import threading
from Functions_and_Var import *

server = conn_server()
PRINTS('\nAguardando a conexão com o cliente...\n')
conn, end = server.accept()
print(f'Conexão aceita!\nIp e porta do cliente conectado: |>{end[0]}, {end[1]}<|')
try:
    
    clients = []
    while True:  
        conn_server, end = server.accept()
        print ("Connection from: ", end)
        clients.append((conn_server, end))
        tClient = threading.Thread(target=Client_Interaction(), args=(conn_server, end))
        tClient.start()
except:
    print('Todas as portas do servidor estão ocupadas')