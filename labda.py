casa = {'rua':'silveira barreto', 'cep':59040010, 'num':1022}
dados = tuple(map (lambda c:casa[c],casa))
print('Este é seu dicionário sem alterações\n')
print(dados)
print('-'*100)
while True:
    add = input('Deseja adicionar mais chaves em seu dicionário?(S/N)').upper()
    print('-'*100)
    if add == 'S':
        chave = input('insira sua chave: ')
        print('-'*100)
        valor = input('Insira o valor da chave: ')
        print('-'*100)
        casa[chave] = valor
        dados = tuple(map (lambda c:casa[c],casa))
        print('Assim ficou seu dicionário\n')
        print(dados)
        print('-'*100)
    elif add == 'N':
        dados = tuple(map (lambda c:casa[c],casa))
        print('Assim ficou seu dicionário\n')
        print(dados)
        print('-'*100)
        break