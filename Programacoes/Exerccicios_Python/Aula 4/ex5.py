import math
print ("Vou calcular a área de um círculo")
n1 = float(input("Digite o raio de um círculo: "))
def area_circulo (r):
    return (math.pi*r**2)
print (f"A área do círculo é {area_circulo(n1):.2f}")
