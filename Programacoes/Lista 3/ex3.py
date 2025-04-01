print ("Vou produzir a tábuada de 0 a 10 de um número")
num = int(input("Digite um número: "))
mult = 1
def fazer_tabuada (numero, multiplicar):

    for i in range (1,11):
        print (f"{numero} x {multiplicar} = {numero*multiplicar}")
        multiplicar +=1

fazer_tabuada(num,mult)