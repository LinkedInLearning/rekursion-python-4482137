def iteriere(daten):
    if isinstance(daten, (list, tuple)):
        for i in daten:
            iteriere(i)
    else:
        print(daten)


# Beispielaufruf

daten = [1, 2, 3, 4, 5]
iteriere(daten)
daten = [1, [2, 3], (4, 5), "abc", ["x", ["y", "z"]]]
iteriere(daten)
