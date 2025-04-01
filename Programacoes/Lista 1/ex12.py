# -*- coding: UTF-8 -*-
print ("digite 2 valores")
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
a = 0
b=0
if n1==n2:
    print ("A e B são iguais")
elif n1>n2:
    b=n1
    a=n2
    print(f"A={a} e B={b}")
elif n2>n1:
    b=n2
    a=n1
    print(f"A={a} e B={b}")
