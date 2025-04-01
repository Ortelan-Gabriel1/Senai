T = [-10, -8, 0, 1, 2, 5, -2, -4]
maior = 0
menor = 0
media=0
for i in T:
    media += i
media = media/len(T)
maior = T[0]
for y in T:
    if y > maior:
        maior = y
menor = T[0]
for y in T:
    if y < menor:
        menor = y
print (f"media = {media}, maior = {maior}, menor = {menor}")


 