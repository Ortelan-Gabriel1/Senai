def Celsius_Fahrenheit(c):
    print (f"{(1.8*c+32):.2f}°Fahrenheit")
def Fahrenheit_Celsius (f):
    print (f"{((f-32)/1.8):.2f}°Celsius")
print ("Posso converter Celsius para Fahrenheit, ou Fahrenheit para Celsius")
escolha = int(input("Digite [1] para converter de Celsius para Fahrenheit, ou Digite [2] para converter de Fahrenheit para Celsius: "))
while escolha != 1 and escolha != 2:
    print ("Digite apenas [1] ou [2]")
    escolha = int(input("Digite [1] para converter de Celsius para Fahrenheit, ou Digite [2] para converter de Fahrenheit para Celsius: "))
if escolha == 1:
    temp = float(input("Digite a temperatura em Celsius: "))
    Celsius_Fahrenheit (temp)
elif escolha == 2:
    temp = float(input("Digite a temperatura em Fahrenheit: "))
    Fahrenheit_Celsius (temp)
else:
    print ("Algo deu errado")
