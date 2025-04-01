print ("digite números e eu vou dizer quantos deles estão entre 100 e 200")
rep = int(input("Quantos números você precisa digitar? "))
cont=0
for v in range (1, rep+1):
    num = float(input(f"Digite o {v}° Valor"))
    if num >= 100 and num<=200:
        cont+=1
print (f"Você digitou {cont} números")