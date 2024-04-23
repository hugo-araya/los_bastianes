# Entero sueldo_base, venta1, venta2, venta3
# Entero total_venta
# Real comision, sueldo_recibir
SALTO = '\n'
sueldo_base = int(input('Sueldo Base: '))
venta1 = int(input('Venta 1: '))
venta2 = int(input('Venta 2: '))
venta3 = int(input('Venta 3: '))
total_venta = venta1 + venta2 + venta3
comision = total_venta * 0.10
sueldo_recibir = sueldo_base + comision
print('Sueldo a recibir: $' + str(sueldo_recibir), SALTO + 'Comision por ventas: $' + str(comision))
