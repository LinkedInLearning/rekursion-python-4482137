def binaer_in_dezimal(binaer, position=0):
    if binaer == 0:
        return 0
    else:
        return (binaer % 10) * (2 ** position) + binaer_in_dezimal(binaer // 10, position + 1)


# Eingabe der Binärzahl
binaerzahl = int(input("Gib eine Binärzahl ein: "))

# Aufruf der rekursiven Funktion
dezimalzahl = binaer_in_dezimal(binaerzahl)

# Ausgabe des Ergebnisses
print("Die Dezimalzahl von", binaerzahl, "ist", dezimalzahl)
