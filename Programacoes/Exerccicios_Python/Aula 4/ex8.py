idade = int(input("Digite a sua idade: "))
def idade_votar (a):
    if idade <16:
        print ("Você é não-eleitor")
    elif idade>=16 and idade<18 or idade > 65:
        print ("Você é eleitor facultativo")
    else:
        print ("Você é eleitor obrigatório")
idade_votar(idade)