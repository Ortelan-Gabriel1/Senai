print ("Vou te dar a tábuada de 0 a 9")
multiplicador=1
num=0
for i in range (0,10):
    for v in range (1,11):
        print (f"{num}x{multiplicador} = {num*multiplicador}")
        multiplicador += 1
    num+=1
    print("=============================================")
    multiplicador=1