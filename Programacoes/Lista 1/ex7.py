# -*- coding: UTF-8 -*-
print("Vou dizer qual o seu salário liquído a partir das suas horas trabalhadas")
hora = int(input("DIgite o total de horas trabalhadas: "))
salario = hora*19.5
desconto = salario*0.9

if salario > 1500.00:
    print(f"seu salário é {desconto}")
elif salario <= 1500.00:
    print(f"seu salário é {salario}")