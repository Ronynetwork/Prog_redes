valor = input('Informe um Valor: ')
aux = valor.replace(' ', '').upper()
posi = len(aux)-1
cont = 0
while posi > cont and aux[cont] == aux[posi]:
    posi -= 1
    cont += 1
if aux[cont] == aux[posi]: print(f"\n ({valor}) é um Palíndromo!\n")
else:
     print(f"\n ({valor}) não é um Palíndromo! ")