import matplotlib.pyplot as plt
#Importa el módulo pyplot y genera el alias plt
X = []
Y = []
x = -16
while x <= 16:
    X.append(x)
    Y.append(x*x)
    x = x + 1
plt.plot(X, Y) # Construye el gráfico.
plt.show()