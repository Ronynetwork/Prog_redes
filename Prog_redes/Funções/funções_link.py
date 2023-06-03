import os, sys

def link_change(link):
    try:
        # fragmenta a URL
        link_quebrado = link.split('/')
        print(link_quebrado)
        # pega apenas o host do fragmento acima
        url_host = link_quebrado[2]
        print(url_host)
        # seleciona o local da imagem
        url_image = '/'+'/'.join(link_quebrado[3:])

        # pega o nome da imagem + extensão

        extensão = link_quebrado[-1].split('.')[-1]
        n_img = link_quebrado[-1].split('.')[0]
        

        # pega apenas a extensão e converte para txt
        arq_txt = n_img.replace(extensão, 'txt')

        # pega o protocolo (HTTP ou HTTPS)
        protocolo = link.split(':')[0]
        return link_quebrado, url_host, url_image, n_img, extensão, arq_txt, protocolo
    except:
        print(f'Erro na fragmentação... {sys.exc_info()[0]}')