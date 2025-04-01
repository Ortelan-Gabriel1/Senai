print ("Vou contar a quantidade de homens e mulheres para você, digite x para encerrar a contagem")
print("Digite M para homens e F para mulheres")
m=0
f=0
while True:
    proc = input("É homem ou mulher?")
    if proc=="x":
        break
    if proc == "M" or "m":
        m+=1
    if proc == "F" or "f":
        f+=1
    if proc != "m" and proc !="M" and proc !="f" and proc !="F" and proc !="x":
        print ("Digite apenas M, F ou x")
print (f"Você contou {f} mulheres e {m} homens")
