def fakultaet_rek(n):
    if n == 0 or n == 1:
        return 1

    return n * fakultaet_rek(n - 1)


zahl = int(input("Geben Sie eine positive Zahl ein: "))
ergebnis = fakultaet_rek(zahl)
print(f"Die Fakultät von {zahl} ist {ergebnis}.")
