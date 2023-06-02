import os, sys

def link_change(link):
    try:
        # fragmenta a URL
        link_quebrado = link.split('/')

        # pega apenas o host do fragmento acima
        url_host = link_quebrado[2]

        # seleciona o local da imagem
        url_image = '/'+'/'.join(link_quebrado[3:])

        # pega o nome da imagem + extensão
        n_img = link_quebrado[-1]
        extensão = n_img.split('.')[-1]

        # pega apenas a extensão e converte para txt
        arq_txt = n_img.replace(extensão, 'txt')

        # pega o protocolo (HTTP ou HTTPS)
        protocolo = link.split(':')[0]
        return url_host, url_image, arq_txt, n_img, extensão, link_quebrado, protocolo
    except:
        print(f'Erro na fragmentação... {sys.exc_info()[0]}')