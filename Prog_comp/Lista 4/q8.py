cpf = int(input('\nInforme o seu CPF: '))
str_cpf = str(cpf) 
qtd_str = len(str_cpf)
if qtd_str == 11:
    posição = 0 
    cont1 = 0 
    qtd_dig = 9 
    multiplicador = 10 
    soma = 0 
    dig_1v = 0 
    dig_2v = 0
    while cont1 < qtd_dig: 
        letra = str_cpf[posição]
        mult = int(letra) * multiplicador 
        soma += mult 
        posição += 1
        cont1 += 1
        multiplicador -= 1 
        if cont1 == qtd_dig:
            dig_2v = (soma * 10)%11 

            if str(dig_2v) == str_cpf[9] and qtd_dig == 9:
                dig_1v = dig_2v
                posição = 0
                cont1 = 0
                multiplicador = 11
                soma = 0
    if str(dig_1v) == str_cpf[9] and str_cpf[10] == str(dig_2v):
        print(f'\nO CPF: {cpf} é válido!\n')
    else:
        print(f'\nO CPF: {cpf} é inválido!\n')
else:
    print('\nInforme um CPF com 11 Caracteres [Somente Números]!\n')