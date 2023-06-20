a = str(input('Digite uma frase qualquer: '))
print(f'A frase que você inseriu foi: {a}\n'); print('Corrigindo os espaços vazios...\n')
a = a.replace(' ', '_')
print(f'A frase corrigida é: {a}'); print('\nFim!')