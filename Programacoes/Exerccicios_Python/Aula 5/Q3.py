notas=[]
media = 0
for i in range (4):
    notas.append (float(input("Digite uma nota: ")))
for i in range (4):
    media += (notas[i])/4
print (f"{media:.2f}")