import matplotlib.pyplot as plt

def zeichne_fraktal(x, y, groesse, tiefe):
    if tiefe == 0:
        # Basisfall: Zeichne ein Quadrat
        plt.fill([x, x + groesse, x + groesse, x, x], [y, y, y + groesse, y + groesse, y], 'k')
    else:
        # Rekursiver Fall: Teile das Quadrat in neun kleinere Quadrate und zeichne den Teppich
        neue_groesse = groesse / 3
        zeichne_fraktal(x, y, neue_groesse, tiefe - 1)  # Linkes oberes Quadrat
        zeichne_fraktal(x + neue_groesse, y, neue_groesse, tiefe - 1)  # Mittleres oberes Quadrat
        zeichne_fraktal(x + 2 * neue_groesse, y, neue_groesse, tiefe - 1)  # Rechtes oberes Quadrat
        zeichne_fraktal(x, y + neue_groesse, neue_groesse, tiefe - 1)  # Linkes mittleres Quadrat
        zeichne_fraktal(x + 2 * neue_groesse, y + neue_groesse, neue_groesse, tiefe - 1)  # Rechtes mittleres Quadrat
        zeichne_fraktal(x, y + 2 * neue_groesse, neue_groesse, tiefe - 1)  # Linkes unteres Quadrat
        zeichne_fraktal(x + neue_groesse, y + 2 * neue_groesse, neue_groesse, tiefe - 1)  # Mittleres unteres Quadrat
        zeichne_fraktal(x + 2 * neue_groesse, y + 2 * neue_groesse, neue_groesse, tiefe - 1)  # Rechtes unteres Quadrat

# Parameter für das Fraktal
x_start = 0
y_start = 0
groesse = 1
tiefe = 4

# Erzeuge ein Figure-Objekt und zeichne das Fraktal
fig, ax = plt.subplots()
ax.set_aspect('equal', 'box')
zeichne_fraktal(x_start, y_start, groesse, tiefe)
plt.xlim(x_start, x_start + groesse)
plt.ylim(y_start, y_start + groesse)
plt.axis('off')
plt.show()
