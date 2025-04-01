nota = int(input("Digite a nota: "))
info = 0
def conceito (a):
    global info
    if nota < 0 or nota>10:
        print ("Digite uma note entre 0 e 10")
    elif nota ==0 or nota< 3:
        print ("Conceito E")
        info =1
    elif nota <=5:
        print ("Conceito D")
        info =1
    elif nota <=7:
        print("Conceito C")
        info =1
    elif nota <=9:
        print("COnceito B")
        info =1
    elif nota == 10:
        print("Conceito A")
        info =1
while info==0:
    nota = int(input("Digite a nota: "))
    conceito(nota)
    

