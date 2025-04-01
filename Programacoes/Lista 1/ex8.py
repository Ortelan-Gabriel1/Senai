# -*- coding: UTF-8 -*-
print("Vou aprovar ou rejeitar sua linha de crédito")
salario = float(input("Digite seu salário bruto: "))
emprestimo = float(input("Digite quanto você pretende emprestar: "))
mes_para_pagar = int(input("Digite em quantos meses você pretende pagar: "))
prestacao = emprestimo/mes_para_pagar
salario30=salario*0.3

if prestacao > salario30:
    print("Você foi rejeitado")
elif prestacao<= salario30:
    print ("Você foi aprovado")