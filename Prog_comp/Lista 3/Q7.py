inicial = int(input('Insira um valor inicial para a P.G:'))
raz = float(input('Insira a razão da sua P.G:'))
qtd_termos = int(input('Insira a quantidade de termos da sua P.G:'))
sel_elem = int(input(f'Insira o enésimo termo que deseja destacar na sua P.G, o termo deve ser menor ou igual a {qtd_termos}:'))
qtd_termos = abs(qtd_termos)
cont = 1
p_g = inicial
soma = 0
n = 0
if inicial and qtd_termos and raz != 0 and sel_elem <= qtd_termos:
    while cont <= qtd_termos:
        print(f'{p_g:.3f}', end = ', ')
        soma = soma + p_g
        p_g *= raz
        cont += 1
        if cont == sel_elem and sel_elem <=qtd_termos:
            n = p_g
    print('Fim da P.G.\n')
    print(f'A soma dos valores da P.G é {soma:.3f}')
    print(f'O elemento referente a {sel_elem}º posição é {n}')
    if raz > 1: print('A P.G é crescente')
    elif raz == 1: print('A P.G é constante')
    elif 0<raz<1: print('A P.G é decrescente')
    else: print('A P.G é oscilante')
else: print('\nInsira os valores corretamente.\n')