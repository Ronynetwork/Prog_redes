palavra = str(input('Insira uma palavra: '))
qtd_letra = len(palavra)
cont = 1
cont1 = 1
cont2 = qtd_letra-1
while cont1 <= (qtd_letra * 2):
    if cont <= qtd_letra:
        print(palavra[:cont])
        cont+=1
    elif cont > qtd_letra:
        print(palavra[:cont2])
        cont2-=1
    cont1+=1