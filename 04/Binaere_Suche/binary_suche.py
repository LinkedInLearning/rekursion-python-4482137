def binaere_suche_rek(daten, ziel, tief, hoch):
    if tief > hoch:
        return -1  # Element wurde nicht gefunden

    mitte = (tief + hoch) // 2

    if daten[mitte] == ziel:
        return mitte  # Element gefunden

    if daten[mitte] > ziel:
        # Suche im linken Teil der Menge
        return binaere_suche_rek(daten, ziel, tief, mitte - 1)
    else:
        # Suche im rechten Teil der Menge
        return binaere_suche_rek(daten, ziel, mitte + 1, hoch)

daten = [1, 3, 5, 7, 9]
ziel = 5
result = binaere_suche_rek(daten, ziel, 0, len(daten) - 1)
print(daten, ziel,"Trefferposition", result, sep=": ")
