def reverse(daten, i):
    if i < 0:
        return
    else:
        print(daten[i])
        reverse(daten, i - 1)


# Beispielzahlen im Tupel
daten = (1, 2, 3, 4, 5)

# Aufruf der rekursiven Funktion
reverse(daten, len(daten) - 1)
# Beispielzahlen mit verschachtelten Daten
daten = (1, (2, 3), 4, 5)

# Aufruf der rekursiven Funktion
reverse(daten, len(daten) - 1)
