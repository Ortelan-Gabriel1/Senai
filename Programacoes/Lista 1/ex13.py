# -*- coding: UTF-8 -*-
print("digite suas 3 notas e vou dizer se você passou, também digite seu número de faltas, vocÊ pode repetir po conta delas")
n1= int(input("digite sua nota: "))
n2= int(input("digite sua nota: "))
n3= int(input("digite sua nota: "))
falta= int(input("digite quantal faltas você fez: "))
media= (n1+n2+n3)/3
if falta>=21:
    print("Você foi reprovado por faltas")
elif media<7:
    print("Você foi reprovado por notas")
elif media>=7:
    print("Você foi aprovado")

