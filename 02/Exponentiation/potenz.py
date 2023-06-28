def pot(basis, exponent):
    if exponent == 0:
        return 1
    else:
        return basis * pot(basis, exponent - 1)


# Eingabe der Basis und des Exponenten
basis = int(input("Gib die Basis ein: "))
exponent = int(input("Gib den Exponenten ein: "))

# Aufruf der rekursiven Funktion
ergebnis = pot(basis, exponent)

# Ausgabe des Ergebnisses
print(basis, "hoch", exponent, "ist", ergebnis)
