print ("Posso conferir se seu número é Bissexto")
ano = int(input("Digite o ano: "))
if ano%4 == 0:
    if ano%100 == 0:
            if ano % 400 ==0:
                print ("Seu ano é Bissexto")
    else:
        print ("Seu ano é Bissexto")
else:
    print ("Seu ano não é Bissexto")
    
          
