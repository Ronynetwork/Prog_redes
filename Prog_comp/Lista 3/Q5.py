valor = 1
while valor != 0:
    valor = int(input('informe o Número: '))
    valor = abs(valor)
    if valor != 0:
        if valor%2 == 0: print('O Número é Par!\n')
        else: print('O Número é Impar!\n')
    else: print('Programa finalizado!')