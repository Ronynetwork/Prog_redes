valor = float(input('Insira um valor inicial da aplicação:'))
taxa = float(input('Insira o valor de taxa mensal desejado:'))
rend = 0
qtd_mes = 1
ano = 12
if valor and taxa != 0:
    while qtd_mes <= ano:
        qtd_mes +=1
        taxa = (1+taxa/100)
        rend_m = valor * (1+taxa)
        rend = valor + rend_m ** ano
        if qtd_mes == ano: break
        a = str (input('Deseja calcular mais um ano?'))
        if a == 's': continue
        elif a == 'n':
            print('Fim da simulação.')
    print(rend)