# Entero cap_invertir
# Real ganancia
cap_invertir = int(input('Monto a invertir: '))
porcentaje = float(input('Porcentaje: '))
ganancia = cap_invertir * porcentaje / 100 
salida = 'Para monto inicial de '+str(cap_invertir)+' la ganacia es de : '+str(ganancia) + ' con un interes del ' + str(porcentaje)+'%.'
print(salida)