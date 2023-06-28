def dezimal_in_binaer(dezimal):
    if dezimal > 0:
        return dezimal_in_binaer(dezimal // 2) + str(dezimal % 2)
    else:
        return ""


# Eingabe der Dezimalzahl
dezimalzahl = int(input("Gib eine Dezimalzahl ein: "))

# Aufruf der rekursiven Funktion
binaerzahl = dezimal_in_binaer(dezimalzahl)

# Ausgabe des Ergebnisses
print("Die Binärzahl von", dezimalzahl, "ist", binaerzahl)
