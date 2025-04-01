import math
print ("Vou calcular a área de um cilindro")
raio = float(input("Digite o raio da base do cilindro: "))
altura = float(input("Digite a altura do cilindro"))
def area_circulo (r):
    return (math.pi*r**2)
def volume (r,h):
    return (area_circulo(r)*h)
print (f"O volume do cilindro é {volume(raio, altura):.2f}")