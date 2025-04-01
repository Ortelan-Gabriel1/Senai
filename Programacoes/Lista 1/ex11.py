# -*- coding: UTF-8 -*-
print("digite suas 2 notas e vou dizer se você passou")
n1= float(input("digite sua nota"))
n2= float(input("digite sua nota"))
media= (n1+n2)/2

if media<3 and media>=0:
    print("Você foi reprovado")
elif media>=3 and media<7:
    print("Você está de recuperação")
elif media>=7 and media:
    print("Você foi aprovado")