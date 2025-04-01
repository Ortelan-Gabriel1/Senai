print ("Está quente ou frio")
while True:

    temperatura = input("Quantos Graus está fazendo hoje")

    if temperatura == "s":
        print ("Finalizando")
        break
    elif int(temperatura) <= 20:
        print ("Está frio")
    elif int(temperatura) > 20  and int(temperatura) < 30:
        print ("Está ameno")
    elif int (temperatura) >= 30:
        print("Tá quente")
    else:
        print ("Algo deu errado")
