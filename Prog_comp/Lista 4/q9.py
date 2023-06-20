palavra_correta = 'MENINO'
aux = palavra_correta
qtd_letras = len(palavra_correta)
acertos = 0
qtd_erros = 6
tentativas = ''
while True:
    letra = str(input('\nInforme uma letra [Poderá errar 6x]: ')).upper()
    repetição = tentativas.find(letra)
    forca = palavra_correta.find(letra)
    if repetição != -1:
        print(f'\nA letra {letra} já foi informada, tente outra!\n')
    elif forca != -1:
        palavra_correta = palavra_correta.replace(letra,'')
        qtd_letras = len(palavra_correta)
        print(f'\nVocê acertou! faltam: {qtd_letras} letras')
        acertos += 1
    else:
        print(f'\nVocê Errou! tem direito a mais: {qtd_erros-1} tentativas.')
        qtd_erros -= 1
    tentativas += letra
    if qtd_erros == 0 or qtd_letras == 0:
         break
if qtd_letras == 0:
    print(f'\nPARABÉNS! VOCÊ GANHOU, a palavra era: {aux}\n')
elif qtd_erros == 0:
    print(f'\nVOCÊ FOI ENFORCADO! Tente Novamente.\n')