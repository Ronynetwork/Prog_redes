import sys, socket, funções_link,ssl


def connect_skt(url_host, url_image):
    url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\nConnection: close\r\n\r\n' 
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    sockt_IPv4 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockt_img = context.wrap_socket(sockt_IPv4, server_hostname=url_host)
    buffer_size = 1024
    
    a,b,c,d,e, protocolo = funções_link.link_change(link_input)
    if protocolo == 'https':
        try:
            sockt_img.connect((url_host, 443))
            sockt_img.send(url_request.encode())
        except:
            print(f'Erro de conexão HTTPS...{sys.exc_info()[0]}')
    elif protocolo == 'http':
        try:
            sockt_img.connect((url_host, 80))
            sockt_img.send(url_request.encode())
        except:
            print(f'Erro de conexão HTTP...{sys.exc_info()[0]}')
    else:
        print(f'Insira um protocolo válido... HTTP ou HTTPS.')

    return url_request, context, sockt_IPv4, sockt_img, buffer_size