def bubble_sort_rek(daten, n=None):
    if n is None:
        n = len(daten)
    if n == 1:
        return daten
    for i in range(n-1):
        if daten[i] > daten[i+1]:
            daten[i], daten[i+1] = daten[i+1], daten[i]
    return bubble_sort_rek(daten, n-1)

daten = [5, 2, 8, 3, 1]
result = bubble_sort_rek(daten)
print(result)
