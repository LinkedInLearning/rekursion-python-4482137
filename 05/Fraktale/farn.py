import matplotlib.pyplot as plt
import random

def zeichne_farn(x, y, iterationen):
    # Startpunkt
    punkte = [(0, 0)]
    
    # Transformationen und Wahrscheinlichkeiten
    transformationen = [
        (0.85, 0.04, -0.04, 0.85, 0, 1.6),
        (0.2, -0.26, 0.23, 0.22, 0, 1.6),
        (-0.15, 0.28, 0.26, 0.24, 0, 0.44),
        (0, 0, 0, 0.16, 0, 0)
    ]
    
    for _ in range(iterationen):
        x, y = transformiere_punkt(x, y, transformationen)
        punkte.append((x, y))
    
    return punkte

def transformiere_punkt(x, y, transformationen):
    transformation = random.choices(transformationen, [t[0] for t in transformationen])[0]
    new_x = transformation[0] * x + transformation[1] * y + transformation[4]
    new_y = transformation[2] * x + transformation[3] * y + transformation[5]
    return new_x, new_y

# Parameter für das Fraktal
x_start = 0
y_start = 0
iterationen = 50000

# Erzeuge Punkte des Farns
punkte = zeichne_farn(x_start, y_start, iterationen)

# Extrahiere x- und y-Koordinaten der Punkte
x_coords, y_coords = zip(*punkte)

# Erzeuge ein Figure-Objekt und zeichne das Fraktal
fig, ax = plt.subplots()
ax.scatter(x_coords, y_coords, s=0.2, c='g', alpha=0.5)
ax.set_aspect('equal', 'box')
plt.axis('off')
plt.show()
