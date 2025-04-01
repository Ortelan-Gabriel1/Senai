# -*- coding: UTF-8 -*-
print("Vou analisar o valor final de um produto")
produto = float(input("DIgite o valor do produto"))
aumento45 = 1.45
aumento30 = 1.30

if produto <20:
    print(f"o valor total do produto é R${produto*aumento45}")
elif produto >=20:
    print(f"o valor total do produto é R${produto*aumento30}")