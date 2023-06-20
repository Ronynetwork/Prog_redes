palavra = input('Informe a palavra a ser verificada: ')
caixa_alta = palavra.upper()
contador = ''
for palíndromo in range(len(caixa_alta),-1,-1):
    contador += caixa_alta[palíndromo]
if contador == caixa_alta:
    print(f'{palavra} é  um Palíndromo')
else:
    print(f'{palavra} é  um Palíndromo')
