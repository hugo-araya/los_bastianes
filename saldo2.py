# Entero cap_inv
# Real p_interes, interes_calculado, saldo
cap_inv = int(input('Dinero: '))
p_interes = float(input('Interes: '))
interes_calculado = cap_inv * p_interes / 100
if interes_calculado > 7000:
    saldo = cap_inv + interes_calculado
    print('Saldo: ', saldo)
else:
    print('Saldo: ', cap_inv)
