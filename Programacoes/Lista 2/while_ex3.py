print ("""Digite a idade de várias pessoas. Vou dizer o total de pessoas com menos de 21 anos. Total de pessoas com mais de 50 anos.
       DIgite -99 para sair""")
num=0
cont21=0
cont50=0
while num !=-99:
    num=int(input("Digite a idade de uma pessoa: "))
    if num>=0:
        if num<21:
            cont21+=1
        if num>50:
            cont50+=1
    if num<0 and num>-99 or num<-99:
        print("Digite apenas números positivos, digite -99 para sair")
print (f"Você digitou a idade de {cont21} pessoas com menos de 21 anos e {cont50} pessoas com mais de 50 anos.")
