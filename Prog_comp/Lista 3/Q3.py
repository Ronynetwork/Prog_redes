val = int(input('Insira um número inteiro positivo:'))
if val>1:
    aux = 1
    while aux <= val:
        cont_div = 0
        div = 1
        while div <= val:
            if aux%div == 0: cont_div +=1
            if cont_div > 2: break
            div +=1
        if cont_div == 2: print(aux, end=', ')
        aux +=1
    print('Fim!')