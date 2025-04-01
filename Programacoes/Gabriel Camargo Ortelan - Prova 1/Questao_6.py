def descobrir_primo (numero):
    div = 0
    for i in range (1,numero+1):
        if numero%i == 0:
            div+=1
    if div==2:
        return (numero)
print ("Vou exibir todos os números primos de 2 até algum número")
num = int(input("Digite um número: "))
while num <=0:
    print("Digite apenas números positivos")
    num = int(input("Digite um número: "))
print (f"Os números primos entre 2 e {num} são: ")
for i in range (2, num):
    if descobrir_primo(i) != None:
        print (descobrir_primo(i))
