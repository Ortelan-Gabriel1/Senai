# -*- coding: UTF-8 -*-
print ("Digite 2 números e vou dizer qual o maior deles")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
if n1>n2:
    print(f"{n1} é maior que {n2}")
elif n2>n1:
    print(f"{n2} é maior que {n1}")
else:
    print("Algo deu errado")