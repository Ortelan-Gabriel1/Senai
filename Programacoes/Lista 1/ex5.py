# -*- coding: UTF-8 -*-
print("Vou dizer se um número é múltiplo de 3")
n1 = int(input("Digite o número: "))
resto = n1%3
if resto == 0:
    print(f"{n1} é múltiplo de 3")
elif resto!=0:
    print(f"{n1} não é múltiplo de 3")