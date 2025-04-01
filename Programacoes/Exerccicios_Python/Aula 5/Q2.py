conjunto = []
print ("Digite 10 números")
for i in range(10):
    num = float(input("Digite um número: "))
    conjunto.append(num)
for i in range (9,-1,-1):
    print (conjunto[i])