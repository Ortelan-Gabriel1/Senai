soma=0 

def soma_impares(a, b):
    global soma
    for i in range (a, b+1):
        if i%2 != 0:
            soma += i
    return soma
n1 = int(input("Digite o 1°número: "))
n2 = int(input("Digite o 2°número: "))
while n2<n1:
    print ("O primeiro número deve ser menor que o segundo")
    n1 = int(input("Digite o 1°número: "))
    n2 = int(input("Digite o 2°número: "))
    
print (f"A soma de todos os números ímpares entre o 1°número e o 2°número é: {soma_impares(n1, n2)}")