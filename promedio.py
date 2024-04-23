# Real Nota1, Nota2, Nota3 Real Promedio
# String Mensaje
nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
promedio = (nota1 + nota2 + nota3) / 3 
if promedio >= 4.0:
    mensaje = 'Estudiante Aprobado'
else:
    mensaje = 'Estudiante Reprobado'
print('Status: ', mensaje)
