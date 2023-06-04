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
        n_img = link_quebrado[-1].split('.')[0]
        if len(n_img) >= 150:
            n_img = n_img[0:150]
        # pega apenas a extensão e converte para txt
        arq_txt = '.txt'
        # pega o protocolo (HTTP ou HTTPS)
        protocolo = link_input.split(':')[0]
        # retirando caracteres que são proibidos de ter no nome de um arquivo, para salvar...
        caracteres_bloqueados = ['/', ':', '*', '?', '|', '<', '>', '"', '\\']
        for x in caracteres_bloqueados: 
            n_img = n_img.replace(x, '')

        return link_quebrado, url_host, url_image, n_img, arq_txt, protocolo
    except:
        print(f'Erro na fragmentação... {sys.exc_info()[0]}')