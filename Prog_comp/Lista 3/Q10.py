valor = int(input('Insira um valor diferente de zero (0 = Encerra a repetição): '))
soma = 0
menor = valor
maior = valor
cont = 0
while valor != 0:
    soma += valor
    cont += 1
    if maior < valor:
        maior = valor
    elif menor > valor:
        menor = valor
    valor = int(input('Insira um valor diferente de zero (0 = Encerra a repetição): '))
media = soma / cont
print(f'A média dos valores é {media}. O maior número foi {maior} e o menor foi {menor}.')