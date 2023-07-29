
def HISTORY(historic, socket_client):
    try:
        msg = f'Esse é seu histórico de comandos:\n\n'
        print(1)
        qtd = 0
        for x in historic:
            print(2)
            qtd +=1
            msg += f'{qtd} {x}\n'
        print(3)
        socket_client.send(msg.encode(CODE))
        print(msg)
    except:
        print(f'Erro no envio do History... {sys.exc_info()[0]}')