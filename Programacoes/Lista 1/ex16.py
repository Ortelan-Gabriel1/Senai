# -*- coding: UTF-8 -*-
print ("Vou dizer a faixa etária de uma pessoa a partir da idade")
idade = int(input("Digite a idade: "))

if idade<2:
    print("É um bebê")
elif idade>=2 and idade>=12:
    print("É uma criança")
elif idade>12 and idade<23:
    print("É um adolescente")
elif idade>=23 and idade<70:
    print("É um adulto")
elif idade>=70:
    print("É um idoso")