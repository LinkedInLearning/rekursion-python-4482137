import matplotlib.pyplot as plt
import numpy as np

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z*z + c
        n += 1
    return n

def zeichne_mandelbrot(xmin, xmax, ymin, ymax, breite, hoehe, max_iter):
    img = np.zeros((hoehe, breite))

    for x in range(breite):
        for y in range(hoehe):
            zx = np.interp(x, [0, breite], [xmin, xmax])
            zy = np.interp(y, [0, hoehe], [ymin, ymax])
            c = complex(zx, zy)
            img[y, x] = mandelbrot(c, max_iter)

    plt.imshow(img.T, cmap='hot', extent=(xmin, xmax, ymin, ymax))
    plt.colorbar()
    plt.xlabel('Real-Teil(c)')
    plt.ylabel('Imaginär-Teil(c)')
    plt.title('Mandelbrot-Menge')
    plt.show()

# Einstellungen für das Mandelbrot-Fraktal
xmin, xmax = -2.5, 1
ymin, ymax = -1.5, 1.5
breite, hoehe = 800, 600
max_iter = 100

# Zeichnen der Mandelbrotmenge
zeichne_mandelbrot(xmin, xmax, ymin, ymax, breite, hoehe, max_iter)
