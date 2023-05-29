import ssl, socket
#url = input('informa a url: ')
link = input('Insira o endereço do arquivo que você deseja baixar:')

# fragmenta a URL
link_quebrado = link.split('/')

# pega apenas o host do fragmento acima
url_host = link_quebrado[2]

# seleciona o local da imagem
url_image = '/'+'/'.join(link_quebrado[3:])

# pega o nome da imagem + extensão
n_img = link_quebrado[-1]
print(n_img)
arq_image = n_img
extensão = arq_image.split('.')[-1]

# pega apenas a extensão e converte para txt
arq_txt = arq_image.replace(extensão, 'txt')

# pega o protocolo (HTTP ou HTTPS)
protocolo = link.split(':')[0]
print('-'*100)
print(f"\nhost: {url_host}\n local_imagem: {url_image}\nnome_imagem: {arq_image}\nextensão: {extensão}\nprotocolo: {protocolo}\n")
print('-'*100)

# Define a porta se a url for HTTP ou HTTPS
if protocolo == 'https':
    buffer_size = 1024 
    url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 

    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    

    sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock_img = context.wrap_socket(sockt, server_hostname=url_host)
    sock_img.connect((url_host, 443))
    sock_img.send(url_request.encode())

    print('\nBaixando a imagem...')
    # Montado a variável que armazenará os dados de retorno
    data_ret = b''
    while True:
        data = sock_img.recv(buffer_size)
        if not data: 
            break
        data_ret += data
    sock_img.close()

    # Separando o Cabeçalho dos Dados
    delimiter = '\r\n\r\n'.encode()
    position  = data_ret.find(delimiter)
    headers   = data_ret[:position]
    image     = data_ret[position+4:]

    print('-'*100,'\n')
    print(str(headers, 'utf-8'),'\n')
    print('-'*100)

    # Salvando a imagem
    file_output = open(n_img, 'wb')
    file_output.write(image)
    file_output.close()

    with open('cabeçalho.txt', 'w', encoding='utf-8') as cabeçalho:
        cabeçalho.write(headers.decode('utf-8'))
