senha = 'sasta2003'
str = input('informe a senha: ')
for contador in range(1000000):
    if str == senha:
        print('\nSenha correta! Bem vindo!\n')
        break
    else: str = input('\nSenha incorreta. Tente novamente \n')