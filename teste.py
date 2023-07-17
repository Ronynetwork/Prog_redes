import sys

mensagens = []
prim_command = (sys.argv[0].split('/')[-1])
mensagens.append(prim_command)

def HISTORY(comunicacao):
    while True:
        comunicacao = input('Insira uma mensagem:')
        HISTORY(comunicacao)
        if comunicacao == 'quit':
            break

        if comunicacao != 'quit':
            print(prim_command)
            mensagens.append(comunicacao)
        else:
            print(mensagens)

