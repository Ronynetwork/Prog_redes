a = int(input('Insira um número inteiro positivo:'))
lista = ''
if a != 0:
    divisor = 1
    contador = 0
    while divisor <= a:
        if a % divisor == 0:
            print(f'Os divisores são {divisor}')
            contador += 1
        divisor += 1
    if contador == 2: print('E o Número é primo!')
    else: print('E o Número não é Primo!')
else: print('Informe um Valor diferente de Zero!')