def gauss_summe(n):
    if n == 1:
        return 1

    return n + gauss_summe(n - 1)


zahl = 10
gauss_sum = gauss_summe(zahl)
print("Die Gauss-Summe von", zahl, "ist:", gauss_sum)
