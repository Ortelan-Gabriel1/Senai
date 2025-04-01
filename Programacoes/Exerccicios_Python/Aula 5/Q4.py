print ("Digite 10 letras")
letra = []
vogal = ["a","e","i,","o","u"]
cont = 10
for i in range (10):
    letra.append (input("Digite uma letra: "))
    for y in range (5):
        if letra[i] == vogal [y]:
            cont -=1
        
print (f"Você digitou {cont} consoantes")