print ("Vou fazer a soma de um número e todos os números antes dele")
num = int(input("Digite um número: "))
soma = 0
while num <=0:
    print("Digite apenas números positivos")
    num = int(input("Digite um número: "))
while num>-1:
    soma += num
    num -=1
print (f"A soma de todos os números é {soma}")
    
