aux = 0
qtd_m = 0
qtd_h = 0
somat = 0
somam = 0
somah = 0
while aux <=5:
    idade = int(input("informe a idade: "))
    sexo = input("selecioe o sexo M(Mulher) e H(Homem)")
    if sexo == "m":
        somat = somat+idade
        somam = somam +idade
        qtd_m +=1
    elif sexo == "h":
        somat = somat+idade
        somah = somah+idade
        qtd_h +=1  
    aux +=1
print(f"a média das idades é {somat/5}. a média das idades femininas {somam/qtd_m} a média das idades masculinax {somah/qtd_h}")