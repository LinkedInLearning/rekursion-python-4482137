def gauss_summe(n):
    if n == 1:
        return 1

    summe = (n * (n + 1)) // 2
    return summe


# Beispielaufruf
zahl = 100
gauss_sum = gauss_summe(zahl)
print("Die Gauss-Summe von", zahl, "ist:", gauss_sum)
