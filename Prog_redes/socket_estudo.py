from socket import *
# METODOS DE UM OBJETO  SOCKET
accept()#Aceita uma conexão com o cliente
bind(endereço)#associa um socket de servidor a um endereço
close()#Fecha um socket, liberando todos os recursos alocados
connect(endereço)#Conecta o cliente a um endereço
connect_ex(endereço)#idem ao item anterior, retornando um indicador de erro em vez de uma exceção, na chamada connect de baixo nível
getpeername()#retona ao socket local o endereço do socket remoto que está conectado
getsockname()#Retorna o endereço do socket local
listen()#começa a escutar pedidos de conexão

# METODOS DE ENVIO E LEITURA DE BYTES
recv()#Lê os bytes recebidos, retornando em uma string atéo tamanho limite do buffer dado pelo buffsize.
recvfrom()#Lê os bytes recebidos, retornando em uma string atéo tamanho limite do buffer dado pelo buffsize.
send()#Solicita o envio dos bytes pelo socket até que um conjunto de bytes seja enviado - buffer suficiente para garantir o envio.
sendall()#envia todos os bytes passados como parâmetro, o que ocasiona sucessivos envios em camadas de sistema até que todos os bytes sejam enviados

#INTERFACE DE SOCKETS
SOCKET_STREAM()#Interface de socket de fluxo(stream), serviço com conexão confiável (TCP), dados enviadossem erros ou duplicação
SOCKET_DGRAM()#Interface de datagrama, define uma conexão por via de (UDP), envios por pacotes independentes. Os dados podem ser perdidos
SOCKET_RAW()#Interface de socketsbrutos. Permite acesso direto a protocolos da camada inferior, como ICMP e IP.

#Criar objeto socket
#Família:
AF_INET()#IPv4
AF_INET6()#IPv6
#Socket:
SOCKET_STREAM()#TCP
SOCKET_DGRAM()#UDP

#Protocolo
Geralmente zero.