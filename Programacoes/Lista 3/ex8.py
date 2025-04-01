def contagem (numero):
    cont=0
    while numero>0:
        numero //= 10
        cont+=1
    return (cont)
        
print ("Vou contar quantos algarismos tem em um número")
num = int(input("Digite um número: "))

while num <0:
    print ("Digite apenas números positivos")
    num = int(input("Digite um número: "))

print (f"O total de algarismos que seu número têm é {contagem (num)}")