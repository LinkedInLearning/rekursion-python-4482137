def permutiere(zahlen):
    # Basisfall: Wenn die Liste leer ist, gibt es keine Permutationen
    if len(zahlen) == 0:
        return [[]]

    permutationen = []  # Liste zur Speicherung der Permutationen

    for i in range(len(zahlen)):
        aktuelle_zahl = zahlen[i]
        # Entferne das aktuelle Element
        verbleibende_zahlen = zahlen[:i] + zahlen[i+1:]

        # Rekursiver Aufruf für die verbleibenden Elemente
        for permutation in permutiere(verbleibende_zahlen):
            permutationen.append([aktuelle_zahl] + permutation)

    return permutationen


zahlen = [1, 2, 3, 4]
ergebnis = permutiere(zahlen)
print(ergebnis)
