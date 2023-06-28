def bubble_sort(daten):
    n = len(daten)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if daten[j] > daten[j+1]:
                daten[j], daten[j+1] = daten[j+1], daten[j]
    return daten

daten = [5, 2, 8, 3, 1]
result = bubble_sort(daten)
print(result)
