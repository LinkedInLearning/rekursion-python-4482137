def finde_minimum(zahlen):
    if len(zahlen) == 0:
        return None

    minimum = zahlen[0]
    for zahl in zahlen:
        if zahl < minimum:
            minimum = zahl

    return minimum


# Beispielaufruf
zahlen = [4, 9, 2, 7, 5, 11, 31, 42, 12, 66, 17]
min_wert = finde_minimum(zahlen)
print("Das Minimum der Zahlen ist:", min_wert)
