n = int(input('Insira um valor inteiro para realizar a sequência de Fibonacci: '))
repet = 1
resultado = 0
n2 = 0
aux = repet
if n != 0:
    print(f'\nSua sequência para N={n} é:')
    while repet <= n:
        resultado = aux + n2
        print(resultado, end=' ')
        repet +=1
        aux = n2
        n2 = resultado
    print(''); print('\nFim da sequência\n')
else: print('\nInsira um valor diferente de 0\n')