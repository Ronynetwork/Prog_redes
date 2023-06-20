vogais = 'aáâeéêiíoóôuú'
palavra = str ( input ( 'Informe a Palavra na qual deseja encontrar as vogais: ' ))
aux = palavra.lower()
qnt = 0
cont = 1
cont1 = 0
cont2 = 1 
for x in range(cont,len(palavra)):
        letra = aux[cont1:cont2]
        encontrar = vogais.find(letra)
        cont += 1
        cont1 += 1
        cont2 += 1
        if encontrar != -1:
            qnt += 1
print ( f'\nA Palavra {palavra} possui o total de: {qnt} vogais!\n' )