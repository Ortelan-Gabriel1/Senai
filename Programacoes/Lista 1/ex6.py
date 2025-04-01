# -*- coding: UTF-8 -*-
print ("Digite 2 números e vou de o primeiro é divisível pelo segundo")
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
resto = a%b
if resto == 0:
    print(f"{a} é divisível por {b}")
elif resto!=0:
    print(f"{a} não é divisível por {b}")