<<<<<<< HEAD
import os, sys
local = os.path.dirname(os.path.abspath(__file__)) 
sys.path.append(local+'//Funções')
import funções_link 

print(local)
'''#url = input('informa a url: ')
link = input('Insira o endereço do arquivo que você deseja baixar:')

# Utilizando de função para modelar a url
url_host, n_img, link_quebrado, extensão, url_image = funções_link.link_change(link)

print('-'*100)
print(f'\nhost:{url_host}\nlocal_imagem:{url_image}')
print(f'\nnome_imagem:{n_img}\nextensão:{extensão}\nprotocolo:{protocolo}\n')
print('-'*100)

# Define a porta se a url for HTTP ou HTTPS
if protocolo == 'https':
    try:
        buffer_size = 1024 
        porta = 443
        url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 
        context = ssl.create_default_context()
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

        sockt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_img = context.wrap_socket(sockt, server_hostname=url_host)
        sock_img.connect((url_host, porta))
        sock_img.send(url_request.encode())
        print('Baixando a imagem...')
    # Montado a variável que armazenará os dados de retorno
        retorno = b''
        while True:
            data = sock_img.recv(buffer_size)
            if not data: 
                break
            retorno += data
        sock_img.close()
        
        # Separando o Cabeçalho dos Dados
        delimiter = '\r\n\r\n'.encode()
        position  = retorno.find(delimiter)
        headers   = retorno[:position]
        image     = retorno[position+4:]

        print('-'*100,'\n')
        print(str(headers, 'utf-8'),'\n')
        print('-'*100)
    except :
        print(f'Erro...{sys.exc_info(0)}')  
        exit()      

elif protocolo =='http':
    try:
        #Identificando a porta e gerando o get
        url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 
        porta   = 80
        buffer_size = 1024
        #Estabelecendo a conexão
        sock_img = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock_img.connect((url_host, porta))
        sock_img.send(url_request.encode())

        print('Baixando a imagem...')

        # Pegando e armazenando o retorno dos dados
        retorno = b''
        while True:
            data = sock_img.recv(buffer_size)
            if not data: 
                break
            retorno += data
        #Fechando a conexão
        sock_img.close()
        delimiter = '\r\n\r\n'.encode()
        position  = retorno.find(delimiter)
        headers   = retorno[:position]
        image     = retorno[position+4:]

        print('-'*100,'\n')
        print(str(headers, 'utf-8'),'\n')
        print('-'*100)

    except :
        print(f'Erro...{sys.exc_info(0)}')  
        exit()      
=======

# Código para realizar commit e push automatico no GITHUB

import subprocess, time, os, platform

if platform.system() == 'Windows':
    os.system('cls')
>>>>>>> 54934b1e3824c521ab9c9539c8a70977329c2986
else:
    os.system('clear')

<<<<<<< HEAD
# Tratamento de caracteres especiais no nome do head
special = [';','.','*','?','/','>','<','|','"']
contem = 0
for letra in special:
    while contem != -1:
        contem = n_img.find(letra)
        n_img = n_img.replace(letra,'-')

# Definindo o local do head
dir_cabeçalho = local + f'\\{n_txt}'

# salvando o head em um arquivo
try:
    with open(n_img, 'w', encoding='utf-8') as header:
        header.write(headers.decode('utf-8'))
except:
    print(f'Erro...{sys.exc_info()[0]}')
=======
print('='*100)
ascii_art = r"""
   _____ _ _   _           _                     _                        _   _             
  / ____(_) | | |         | |         /\        | |                      | | (_)            
 | |  __ _| |_| |__  _   _| |__      /  \  _   _| |_ ___  _ __ ___   __ _| |_ _  ___  _ __  
 | | |_ | | __| '_ \| | | | '_ \    / /\ \| | | | __/ _ \| '_ ` _ \ / _` | __| |/ _ \| '_ \ 
 | |__| | | |_| | | | |_| | |_) |  / ____ \ |_| | || (_) | | | | | | (_| | |_| | (_) | | | |
  \_____|_|\__|_| |_|\__,_|_.__/  /_/    \_\__,_|\__\___/|_| |_| |_|\__,_|\__|_|\___/|_| |_|
                                                                                            
                                     by - kakanetwork
 """                                                                                                                       
print(ascii_art)

print('='*100)

def Git_Push ():
    print('='*100)
    modo = ''
    while modo not in ['A', 'U', 'S', '?']:
        modo = str(input('\nModos:\nA - Automatico\nU - Único\nS - Sair\n? - Ajuda\n\nQual você deseja? ').upper())
        if modo not in ['A', 'U', 'S', '?']:
            print('Tente Novamente... informe corretamente!')
    
    commit_name = 'Atualizado'
    branch_origin = 'home'
    tempo_seg = 120
    print('')
    print('='*100)
    if modo == 'A':
        while True:
            subprocess.run(['git', 'add', '.'])
            subprocess.run(['git', 'commit', '-m', commit_name])
            subprocess.call(["git", "push", "-u", "origin", branch_origin])
            print('='*100)
            time.sleep(tempo_seg) 

    elif modo == 'U':
        print('')
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-m', commit_name])
        subprocess.call(["git", "push", "-u", "origin", branch_origin])
        print('\nVolte sempre!\nby kakanetwork')
        print('\n'+'='*100)

    elif modo == '?':
        print(f'\nExplicação das Variavéis:\n\nAutomático -> Será gerado um Commit a cada {tempo_seg}s até que você encerre o programa! (se desejar alterar os segundos, acesse a configuração)\n\
Único -> Será gerado um Commit Único e o Programa será encerrado!\n\nCommit_name -> O nome do seu commit, pode ser genérico (se necessário alteração, vá nas configurações)!\n\
Branch_Origin -> O nome do seu branch default no Github (se necessário alteração, vá nas configurações)!\n')
        print('='*100)
    elif modo == 'S':
        print('\nPrograma Encerrado com Sucesso! :(\n')
        exit()

def Git_Pull ():
    print('='*100)
    print('')
    subprocess.run(['git', 'pull'])
    print('\nVolte sempre!\nby kakanetwork')
    print('\n'+'='*100)

def Git_Connect ():
    print('='*100)
    print('\nem desenvolvimento...')

def Ajuda ():
    print('='*100)
    print(f'\nGit Push -> Realiza o Push do seus Commits, ou seja leva a atualização deles para o seu github\nGit Pull -> Realiza o Pull dos seus commits, \
ou seja traz as atualizações do seu código no github para seu ambiente de programação\nGit Connect -> Vai realizar a conexão do seu github com o seu VSCODE \
automaticamente (Recomendado realizar antes de qualquer Pull ou Push.)!\n')
    print('='*100)

def Sair ():
    print('='*100)
    print('\nPrograma Encerrado com Sucesso! :(')
>>>>>>> 54934b1e3824c521ab9c9539c8a70977329c2986
    exit()

opções = {
    '1': Git_Push,
    '2': Git_Pull,
    '3': Git_Connect,
    '4': Ajuda,
    '5': Sair
}   

<<<<<<< HEAD
# Localizando o arquivo cabeçalho
dir_cabeçalho = local + f'\\{n_img}'
=======
opções_descritivas = {
    '1': 'Realizar Push no GitHub',
    '2': 'Realizar Pull do GitHub',
    '3': 'Conectar ao GitHub',
    '4': 'Exibir Ajuda',
    '5': 'Sair do Programa'
}
>>>>>>> 54934b1e3824c521ab9c9539c8a70977329c2986

print('\nFerramentas Disponiveis:\n')

<<<<<<< HEAD
# Salvando a imagem com a nova extensão
nome_final = 'imagem.' + extensão_head
imagem = local + f'\\{n_img}'

try:
    with open(imagem, 'wb') as img:
        img.write(image)
except:
    print(f'Erro...{sys.exc_info()[0]}')
    exit()
'''
=======
for key, value in opções_descritivas.items():
    print(f'{key}: {value}')

ferramenta = ''

while ferramenta not in opções:
    ferramenta = input('\nQual Ferramenta deseja utilizar? ')
    if ferramenta not in opções:
        print('Tente Novamente... informe corretamente!')

print(f'Você escolhou a ferramenta: {opções_descritivas[ferramenta]}\n')
opções[ferramenta]()
>>>>>>> 54934b1e3824c521ab9c9539c8a70977329c2986
