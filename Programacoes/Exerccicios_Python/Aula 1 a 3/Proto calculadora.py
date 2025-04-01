print("Posso fazer operações para você")
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
 
print ("Qual operação você deseja realizar?")
print ("divisão , multiplicação , adição , subtração ")
calculo = input("Digite a operação desejada: ")

if calculo == "divisão" or "divisao":
    print(f"O resultado é {numero1/numero2:.2f}")
elif calculo == "multiplicação" or "multiplicacao":
    print(f"O resultado é {numero1*numero2}")
elif calculo == "adição" or "adicao":
    print(f"O resultado é {numero1+numero2}")
elif calculo == "subtração" or "subtracao":
    print(f"O resultado é {numero1-numero2}")
else:
    print ("Algo de errado")