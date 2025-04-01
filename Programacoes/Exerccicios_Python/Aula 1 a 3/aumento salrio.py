salario = float(input("QUal o seu saário?"))
aumento10 = 1.10
aumento15 = 1.15
if salario > 1250.00:
    print (f"Seu salário recebeu um aumento de 10% agora o valor dele é R${aumento10*salario}")
else:
    print (f"Seu salário recebeu um aumento de 15% agora o valor dele é R${aumento15*salario}")