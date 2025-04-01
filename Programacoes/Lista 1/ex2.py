# -*- coding: UTF-8 -*-
import math
print ("Digite um número, caso ele for positivo, vou dar sua raiz quadrada, se ele for negativo, vou dar seu quadrado")
n = int(input("digite um número"))

if n>=0:
    quadrada =  math.sqrt(n)
    print (f"O resultado da raiz quadrada de {n} é {quadrada:.2f}")

elif n<0:
    potencia = n**2
    print(f"O quadrado de {n} é {potencia}")
else:
    print("Algo deu errado, não digite números com vírgula")