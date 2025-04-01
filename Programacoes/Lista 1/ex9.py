# -*- coding: UTF-8 -*-
print("Vou determinar se você esta com um peso favorável IMC (Índice de Massa Corpórea)")
peso= float(input('Digite seu peso: '))
altura= float(input('Digite sua altura: '))
imc = peso/(altura*altura)

if imc < 20:
    print ('Você está abaixo do peso')
elif imc >= 20 and imc<25:
    print ('Você está no peso normal')
elif imc >= 25 and imc<30:
    print ('Você está no sobre peso')
elif imc >= 30 and imc<40:
    print ('Você está obeso')
else:
    print ("você está obeso mórbido")