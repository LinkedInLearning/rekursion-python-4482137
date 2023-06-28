import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_menge_rekursiv(z, c, max_iter):
    if max_iter == 0:
        return 0

    if np.abs(z) > 2:
        return max_iter

    z_neu = z**2 + c
    return mandelbrot_menge_rekursiv(z_neu, c, max_iter - 1)

def mandelbrot_menge(breite, höhe, xmin, xmax, ymin, ymax, max_iter):
    # Erzeugung des Gitters
    x = np.linspace(xmin, xmax, breite)
    y = np.linspace(ymin, ymax, höhe)
    X, Y = np.meshgrid(x, y)
    Z = X + 1j * Y

    # Initialisierung der Ausgabematrix
    ausgabe = np.zeros(Z.shape, dtype=int)

    # Berechnung der Mandelbrot-Menge
    for i in range(höhe):
        for j in range(breite):
            c = Z[i, j]
            ausgabe[i, j] = mandelbrot_menge_rekursiv(0, c, max_iter)

    return ausgabe

# Parameter für das Mandelbrot-Set
breite = 600
höhe = 600
xmin, xmax = -2.5, 1
ymin, ymax = -1.5, 1.5
max_iter = 100

# Erzeugung der Mandelbrot-Menge
mandelbrot = mandelbrot_menge(breite, höhe, xmin, xmax, ymin, ymax, max_iter)

# Visualisierung der Mandelbrot-Menge
plt.figure(figsize=(10, 10))
plt.imshow(mandelbrot, extent=(xmin, xmax, ymin, ymax), cmap='hot', origin='lower')
plt.title('Mandelbrot-Menge')
plt.xlabel('Re(c)')
plt.ylabel('Im(c)')
plt.colorbar(label='Anzahl der Iterationen')
plt.show()
