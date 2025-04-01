print("Vou falar a média dos números que você escolhar")
quant = int(input("Quantos números você deseja colocar? "))
num_coloc = 1
numero = 0
for v in range (1,quant+1):
    numero += int(input(f"Digite o {v}° número: "))
media = numero/quant
print (f"A média dos números digitados é {media}")
