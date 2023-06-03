import sys

def link_change(link_input):
    try:
        # fragmenta a URL
        link_quebrado = link_input.split('/')
        print(link_quebrado)
        # pega apenas o host do fragmento acima
        url_host = link_quebrado[2]
        print(url_host)
        # seleciona o local da imagem
        url_image = '/'+'/'.join(link_quebrado[3:])

        # pega o nome da imagem + extensão

        extensão = link_quebrado[-1].split('.')[-1]
        n_img = link_quebrado[-1].split('.')[0]
        print(n_img)
        # pega apenas a extensão e converte para txt
        arq_txt = n_img.replace(extensão, '.txt')

        # pega o protocolo (HTTP ou HTTPS)
        protocolo = link_input.split(':')[0]
        return link_quebrado, url_host, url_image, n_img, extensão, arq_txt, protocolo
    except:
        print(f'Erro na fragmentação... {sys.exc_info()[0]}')
    


def extension_head (headers):
    chave = 'Content-Type:'
    try:
        line = headers.strip().split('\n')
        for x in line:
            if x.find(chave):
                extensão_head = x.strip().split('/')[1]
                break
        html_verification = extensão_head.find(';')
        if html_verification != -1:
            extensão_head = extensão_head.split(';')[0]
        return extensão_head
    except:
        print(f'Erro na obtenção da extensão... {sys.exc_info()[0]}')