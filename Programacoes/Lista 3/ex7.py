def adicao (n1, n2):
    return (n1 + n2)
def subtracao (n1, n2):
    escolha = int(input(f"Digite [1] se vc deseja subitrair {n1} por {n2}, ou digite [2] se você deseja subtrair {n2} por {n1}: "))
    while escolha != 1 and escolha!= 2:
        escolha = int(input(f"Digite [1] se vc deseja subtrair {n1} por {n2}, ou digite [2] se você deseja subtrair {n2} por {n1}: "))
    if escolha == 1:
        return (n1-n2)
    elif escolha == 2:
        return(n2-n1)
def divicao (n1, n2):
    escolha = int(input(f"Digite [1] se vc deseja dividir {n1} por {n2}, ou digite [2] se você deseja dividir {n2} por {n1}: "))
    while escolha != 1 and escolha!= 2:
        escolha = int(input(f"Digite [1] se vc deseja dividir {n1} por {n2}, ou digite [2] se você deseja dividir {n2} por {n1}: "))
    if escolha == 1:
        return (n1/n2)
    elif escolha == 2:
        return(n2/n1)
def multiplicacao (n1, n2):
    return (n1*n2)


print ("Vou fazer cálculos para você")
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
sinal = input ("Digite [+] para adição, [-] para subtração, [/] para divisão, ou [x] para multiplicação: ")
while sinal != "+" and sinal != "-" and sinal != "/" and sinal != "x":
    sinal = input ("Digite [+] para adição, [-] para subtração, [/] para divisão, ou [x] para multiplicação: ")

if sinal == "+":
    print (f"O resultado da soma é {adicao(n1,n2)}")
elif sinal == "-":
    print (f"O resultado da subtração é {subtracao(n1,n2)}")
elif sinal == "/":
    print (f"O resultado divisão é {(divicao(n1,n2)):.2f}")
elif sinal == "x":
    print (f"O resultado da multiplicação é {multiplicacao(n1,n2)}")

