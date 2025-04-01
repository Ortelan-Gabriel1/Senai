print ("Vou verificar se você possuí desconto pela sua idade e qual será o novo valor da compra com o desconto")
compra = int(input("Digite o valor da compra: "))
idade = int (input("Digite a sua idade: "))
desconto = compra/10
while compra <=0 or idade <=0:
    print ("Digite apenas valores positivos")
    compra = float(input("Digite o valor da compra: "))
    idade = int (input("Digite a sua idade: "))
    desconto = compra/10
if idade >60:
    print (f"Você recebeu um desconto de R${desconto:}, ele representa 10% da sua compra, o valor total da sua compra, após a aplicação do desconto, é de R${compra-desconto}")
else:
    print (f"Você não recebeu desconto, o valor da sua compra é de {compra}")

             
