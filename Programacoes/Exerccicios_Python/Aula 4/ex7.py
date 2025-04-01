custo = float(input("Digite o custo do produto: "))
taxaImposto= float(input("Digite o imposto do produto: "))
def somaImposto (a,b):
    return (a+a*(b/100))
print (f"O custo do produto com imposto é de R${somaImposto(custo, taxaImposto):.2f}")
