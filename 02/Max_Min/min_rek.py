def finde_minimum(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        min_rest = finde_minimum(lst[1:])
        if lst[0] < min_rest:
            return lst[0]
        else:
            return min_rest


# Beispielaufruf
zahlen = [4, 9, 2, 7, 5, 11, 31, 42, 12, 66, 17]
min_wert = finde_minimum(zahlen)
print("Das Minimum der Zahlen ist:", min_wert)
