print ("Vou te dar o fatorial de um número:")
num = int(input("Digite um número: "))
fat=1
fatorial = f"{num}"
for i in range (num, 1, -1):
    fat = i*fat
    fatorial += f"x{i-1}"
print (f"""O fatorial de {num} é {fat}
{num}!={fatorial}""")