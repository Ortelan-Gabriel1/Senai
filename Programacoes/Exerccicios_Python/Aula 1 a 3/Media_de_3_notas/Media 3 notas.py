print("pigite suas 3 notas")
n1= int(input("digite sua nota"))
n2= int(input("digite sua nota"))
n3= int(input("digite sua nota"))
media= (n1+n2+n3)/3

if media<5 and media>=0:
    print("REprovado seu inutil")
elif media>=5 and media<7:
    print("recuperação")
elif media>=7 and media<10:
    print("aprovado")
