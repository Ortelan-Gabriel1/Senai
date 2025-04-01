import time
print ("Vou fazer uma contagem regressiva")
cont = int(input("Digite um número: "))
def  regressiva (a):
    for i in range (a,0,-1):
        print (i)
        time.sleep(0.5)
    print ("Parabéns")
regressiva (cont)