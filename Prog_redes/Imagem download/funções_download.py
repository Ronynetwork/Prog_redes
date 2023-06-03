import sys, socket,ssl

def connect_http(url_host, url_image):
    url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\nConnection: close\r\n\r\n' 
    socket_img = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        socket_img.connect((url_host, 80))
        socket_img.send(url_request.encode())
    except:
        print(f'Erro de conexão HTTP...{sys.exc_info()[0]}')
        exit()
    return socket_img

def connect_https(url_host, url_image):
    url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\nConnection: close\r\n\r\n'    # define a requisição 
    context = ssl.create_default_context()      # criação do contexto SSL para conexão HTTPS
    context.check_hostname = False      # desativa a verificação do nome do host durante a autenticação SSL.
    context.verify_mode = ssl.CERT_NONE     # o certificado do servidor não será verificado
    socket_TCP_IPV4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)     # criação do socket/ conexão com o server (IPV4/TCP)
    socket_img = context.wrap_socket(socket_TCP_IPV4, server_hostname=url_host)     # Envolve o socket criado anteriormente em uma conexão segura (wrap_socket)
    
    try:
        socket_img.connect((url_host,443))
        socket_img.sendall(url_request.encode('utf-8'))
    except:
        print(f'Erro de conexão HTTPS... {sys.exc_info()[0]}')
        exit()
    return socket_img