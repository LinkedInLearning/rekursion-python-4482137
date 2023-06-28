def quicksort_rek(daten):
    if len(daten) <= 1:
        return daten
    
    pivot = daten[len(daten)//2]  # Wähle das Pivot-Element in der Mitte der Liste
    links = [x for x in daten if x < pivot]  # Elemente kleiner als das Pivot
    mitte = [x for x in daten if x == pivot]  # Elemente gleich dem Pivot
    rechts = [x for x in daten if x > pivot]  # Elemente größer als das Pivot
    
    # Rekursiv sortiere die Teillisten
    return quicksort_rek(links) + mitte + quicksort_rek(rechts)

daten = [4, 2, 3, 1, 5, 1, 6, 3]
result = quicksort_rek(daten)
print(result)
