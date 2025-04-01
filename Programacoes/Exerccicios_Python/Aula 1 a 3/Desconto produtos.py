print ("Eu posso calcular descontos")

preco = float (input("digite o valor do produto: "))
porce = input ("digite a porsentagem desejada: ")

porce0= float(porce[:-1])
desc= preco*(porce0/100)
desct= preco-desc

print ("O desconto foi de: ", desc)
print ("sO preço total agora é de:", desct)
