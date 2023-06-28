def maximum_berechnen(zahlen):
    if len(zahlen) == 0:
        return None

    maximum = zahlen[0]
    for zahl in zahlen:
        if zahl > maximum:
            maximum = zahl

    return maximum


# Beispielaufruf
zahlen = [4, 9, 2, 7, 5, 11, 31, 42, 12, 1, 66, 17]
max_wert = maximum_berechnen(zahlen)
print("Das Maximum der Zahlen ist:", max_wert)
