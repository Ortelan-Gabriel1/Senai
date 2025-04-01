print("Vou falar a média dos números que você digitar")
numero = 0
quant=0
soma=0
while numero >= 0:
    numero = int(input(f"Digite o {quant+1}° número: "))
    if numero >=0:
        soma+=numero
        quant+=1
media = soma/quant
print (f"A média dos números digitados é {media:.2f}")