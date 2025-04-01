num = int(input("Digite um número e vou dizer se ele é primo: "))

def descobrir_primo (numero):
    div = 0
    for i in range (1,numero+1):
        if numero%i == 0:
            div+=1
    if div ==0:
        print (f"O número {num} é primo")
    else:
        print (f"O número {num} não é primo")
descobrir_primo (num)