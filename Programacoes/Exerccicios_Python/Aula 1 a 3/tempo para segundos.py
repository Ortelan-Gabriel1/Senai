print ("Transformo uma certa quantidade de tempo em segundos")

dias=int(input("Digite o valor de Dias "))
hora=int(input("Digite o valor de horas "))
minutos=int(input("Digite o valor de minutos "))
seg=int(input("Digite o valor de Segundos "))

soma = (dias*24*60*60) + (hora*60*60) + (minutos*60) + seg

print ("OS segundos todais são: ", soma)
