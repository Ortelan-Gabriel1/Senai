print ("Posso aprovar empréstimos")
casa = float(input("Qual o valor da casa a comprar?"))
salario = float(input("Qual o valor do seu salario?"))
anos = float(input("Em quantos anos você pretende pagar?"))
preco_mes = casa/(anos*12)
salario30 = salario*0.3

if salario30<preco_mes:
    print ("Você não foi aprovado")
else:
    print ("Você foiaprovado")