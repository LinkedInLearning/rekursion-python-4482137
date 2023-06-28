def ggT(a, b):
    if b == 0:
        return a
    else:
        return ggT(b, a % b)
# Eingabe der Zahlen
zahl1 = int(input("Gib die erste Zahl ein: "))
zahl2 = int(input("Gib die zweite Zahl ein: "))
# Aufruf der rekursiven Funktion
ergebnis = ggT(zahl1, zahl2)
# Ausgabe des Ergebnisses
print("Der größte gemeinsame Teiler von", zahl1, "und", zahl2, "ist", ergebnis)
