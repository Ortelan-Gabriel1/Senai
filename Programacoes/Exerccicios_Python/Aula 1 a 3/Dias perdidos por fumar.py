print("Vou calcular quanto tempo de vida você já perdeu por fumar")
cpd = float(input("digite quantos cigarros você fuma por dia: "))
qa = float(input("Digite a quantos anos você fuma: "))

fumod =(qa*365*cpd*10)
dp=int((fumod//60)//24)

print(f"Você já perdeu {dp} dias da sua vida")
