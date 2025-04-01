# -*- coding: UTF-8 -*-
print ("Me dê 3 números para utilizar como aresta, vou dizer se você pode ou não formar um triângulo com eles")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

if n1>n2+n3 or n2>n1+n3 or n3>n2+n1:
    print ("Você não pode fazer um triângulo com esses valores de arestas")
elif n1!=n2 and n1!=n3 and n3!=n2:
    print ("Você pode fazer um triângulo escaleno com esses valores de arestas")
elif n1 == n2 or n1==n3 or n3==n2:
    print ("Você pode fazer um triângulo isósceles com esses valores de arestas")
elif n1==n2 and n1==n3 and n3==n2:
    print ("Você pode fazer um triângulo equilátero com esses valores de arestas")