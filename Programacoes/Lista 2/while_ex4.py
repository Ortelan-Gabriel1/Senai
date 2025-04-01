print ("""Vou ler vários números inteiros positivos e mostrarei, no final, a soma dos números pares digitados, e a soma dos números ímpares digitados.
       Digite um número maior que 1000 para sair""")
num=0
impar=0
par=0
while num <=1000:
    num=int(input("Digite um número: "))
    if num>=0 and num<=1000:
        if num%2 == 0:
            par+=num
        if num%2 !=0:
            impar+=num
    if num<0 and num>-99 or num<-99:
        print("Digite apenas números positivos.")
print (f"A soma de todos os númaros pares digitados é {par} e a soma de todos os númaros ímpares digitados é {impar}.")