vel=float(input("Qual a velocidade do seu carro?"))
multa=(vel-80) * 5
if vel>80:
    print ("Você foi multado")
    print (f"O valor da multa é R${multa}")
else:
    print ("Você está dentro da velocidade permitida 😁")