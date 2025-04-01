print ("Vou calcular a comissão de uma venda")
venda = float(input("Digite o valor da venda: "))
comissao_5 = (venda/100)*5
comissao_8 = (venda/100)*8
while venda <=0:
    print("Digite apenas valores positivos")
    venda = float(input("Digite o valor da venda: "))
    comissao_5 = (venda/100)*5
    comissao_8 = (venda/100)*8
if venda<=5000:
    print (f"A comissão recebida será de R${comissao_5}")
elif venda>5000:
    print (f"A comissão recebida será de R${comissao_8}")

    
