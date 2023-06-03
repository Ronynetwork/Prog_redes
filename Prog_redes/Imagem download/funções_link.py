import sys
#url = input('informa a url: ')

def link_change():
    try:
        #url = input('informa a url: ')
        link_input = input('Insira o endereço do arquivo que você deseja baixar:')
        # fragmenta a URL
        link_quebrado = link_input.split('/')

        # pega apenas o host do fragmento acima
        url_host = link_quebrado[2]

        # seleciona o local da imagem
        url_image = '/'+'/'.join(link_quebrado[3:])

        # pega o nome da imagem + extensão
        extensão = link_quebrado[-1].split('.')[1]
        print(extensão)
        n_img = link_quebrado[-1].split('.')[0]
        print(n_img)
        # pega apenas a extensão e converte para txt
        arq_txt = n_img + '.txt'
        print(arq_txt)
        # pega o protocolo (HTTP ou HTTPS)
        protocolo = link_input.split(':')[0]

        return link_quebrado, url_host, url_image, n_img, extensão, arq_txt, protocolo
    except:
        print(f'Erro na fragmentação... {sys.exc_info()[0]}')
    

def content_type (headers): # FUNÇÃO PARA RETIRAR O CONTENT-TYPE DO HEADER DE UM ARQUIVO
    try:
        linhas = headers.strip().split('\n') # pego o header já decodificado e quebro ele em linhas
        for x in linhas:
            if x.startswith('Content-Type:'): # vasculho nessas linhas o content-type por meio do startswich que retorna True quando a palavra existir
                extensão = x.strip().split('/')[1] # pego a linha do Content-type, retiro os espaços com strip() e quebro com split() onde tiver uma barra
                break # com isso para o for, pois já tenho a extensão
        html_verification = extensão.find(';') # EXCEÇÃO: quando a url é de um arquivo HTML, temos que fazer um filtro diferente para conseguir pegar a extensão
        if html_verification != -1:
            extensão = extensão.split(';')[0] # usamos split() para quebrar a extensão onde tiver ';' e pego o primeiro resultado 
                                              # formato content type HTML -> html; charset = utf-8
        return extensão
    except:
        print(f'\nErro na captura do Content-Type...{sys.exc_info()[0]}\n')
        