num = int(input("Digite um número e vou dizer se ele é primo: "))
div = 0
for i in range (1,num+1):
    if num%i == 0:
        div+=1
if div ==0:
    print ("Seu número é primo")
else:
    print ("Seu número não é primo")