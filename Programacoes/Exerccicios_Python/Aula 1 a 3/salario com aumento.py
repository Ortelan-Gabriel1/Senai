print ("Vou aumentar seu salário")

salario = float (input("digite o salário que precisa de aumento: "))
porce = input ("digite a porsentagem desejada: ")

porce0= float(porce[:-1])
aumento= salario*(porce0/100)
aumentot= salario+aumento

print ("O aumeto foi de: ", aumento)
print ("seu salário agora é de:", aumentot)
