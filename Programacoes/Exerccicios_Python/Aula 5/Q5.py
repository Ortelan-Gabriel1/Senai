print ("Vou juntar 2 listas")
print ("Digite a primeira lista, digite fim para finaliza-la")
resposta = []
lista1=[]
lista2=[]
lista3=[]
while True:
    resposta = input ("Digite um valor: ")
    if resposta == "fim" or resposta=="Fim":
        break
    else:
        lista1.append(resposta)
        resposta = []

print ("Digite a Segunda lista, digite fim para finaliza-la")
resposta = []
while True:
    resposta = input ("Digite um valor: ")
    if resposta == "fim" or resposta=="Fim":
        break
    else:
        lista2.append(resposta)
        resposta = []

lista3.extend (lista1) 
lista3.extend (lista2)
print (lista1)
print (lista2)
lista3.sort
print (lista3)