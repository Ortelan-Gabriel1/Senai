print("Digite números e eu vou falar qual é o menor e qual o maior que vovê digitou")
numero = int(input("Digite um número: "))
num_maior=numero
num_menor=numero
while numero >= 0:
    numero = int(input("Digite um número: "))
    if numero >=0:
        if numero >= num_maior:
            num_maior=numero
        if numero <= num_menor:
            num_menor=numero
print (f"O maior número digitado é {num_maior} e o menor é {num_menor}")