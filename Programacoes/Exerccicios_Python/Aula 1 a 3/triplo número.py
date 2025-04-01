print ("Digite um número e vou dar o triplo dele, digite -999 para encerrar o programa")
while True:
    num = int(input("Digite um número: "))
    if num == -999:
        break
    print (f"O triplo de {num} é {num*3}")
print("Processo encerrado")
