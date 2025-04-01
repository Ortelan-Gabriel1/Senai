print ("Coloque 3 números e descubra qual o maior")
N1 = int(input("coloque o primeiro número"))
N2 = int(input("coloque o primeiro número"))
N3 = int(input("coloque o primeiro número"))

if N1==N2 or N1==N3 or N2==N3:
        print("Err0, não coloque números iguais seu idiota")
elif N1>N2 and N1>N3:
         print("O primeiro é o maior número")
elif N2>N1 and N2>N3:
         print("O segundo é o maior número")
elif N3>N1 and N3> N2:
         print("O terceiro é o maior número")
    
