# -*- coding: UTF-8 -*-
print("Vou determinar como está a temperatura atual")
temperatura= float(input('Digite a temperatura em graus celsius: '))


if temperatura <= 15:
    print ('Está muito frio')
elif temperatura > 15 and temperatura<=23:
    print ('Está Frio')
elif temperatura > 23 and temperatura<=26:
    print ('Está Agradavél')
elif temperatura > 26 and temperatura<=30:
    print ('Está calor')
else:
    print ("Está muito quente")