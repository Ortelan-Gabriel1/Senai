# -*- coding: UTF-8 -*-
print("Vou fazer a soma de 2 números, se ele for maior que 20, vou somar mais 8, se for menor que 20, vou subtrair 5")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = n1 +n2

if soma>20:
    print (f"O valor da soma, mais 8, é: {soma+8}")
if soma<=20:
    print (f"O valor da soma, menos , é: {soma-5}")