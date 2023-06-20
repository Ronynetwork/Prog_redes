an1 = str(input('Informe a Primeira Palavra do Anagrama: '))
an2 = str(input('Informe a Segunda Palavra do Anagrama: '))
aux_an1, aux_an2 = an1.upper(), an2.upper()
qtd_an2 = len(an2)
if len(an1) == qtd_an2:
    cont = 0
    cont1 = 1
    cont2 = 1
    cont3 = 1
    ultimo_dig = aux_an1[-1] in aux_an2 and aux_an2[-1] in aux_an1
    while cont1 < qtd_an2:
        anagrama = aux_an2.find(aux_an1[cont:cont2])
        cont+=1
        cont1 += 1
        cont2 += 1
     
        if anagrama != -1 and ultimo_dig == True:
             cont3 += 1
    if cont3 == qtd_an2:
        print(f'Sua palavra é um anagrama')
    else:
        print(f'{an1} Não é Anagrama de {an2}')
else:
    print(f'{an1} Não é Anagrama de {an2}')