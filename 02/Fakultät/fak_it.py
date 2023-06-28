def fakultaet_it(n):
    fakultaet = 1
    if n == 0:
        return fakultaet
    else:
        for i in range(1, n + 1):
            fakultaet *= i
        return fakultaet


zahl = int(input("Geben Sie eine positive Zahl ein: "))
ergebnis = fakultaet_it(zahl)
print(f"Die Fakultät von {zahl} ist {ergebnis}.")
