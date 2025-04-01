# -*- coding: UTF-8 -*-
print("Vou dizer se um número é par ou ímpar")
n1 = int(input("Digite o número: "))
resto = n1%2
if resto == 0:
    print(f"{n1} é par")
elif resto!=0:
    print(f"{n1} é ímpar")