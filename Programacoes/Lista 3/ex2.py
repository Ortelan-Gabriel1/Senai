def mult_digitos (numero, multiplicacao, digito):
    while numero>0:
        digito = numero%10
        numero //= 10
        if digito > 0:
            multiplicacao *= digito
    return (multiplicacao)


print ("vou calcular o produto de todos os dígitos de um número inteiro")
num = int(input("Digite um número: "))
mult=1
digito=0
while num <0:
    print ("Digite apenas números positivou")

print (f"O produto de todos os dígitos é {mult_digitos (num, mult, digito)}")
