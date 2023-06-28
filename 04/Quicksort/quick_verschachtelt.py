def quicksort_rek(daten):
    if len(daten) <= 1:
        return daten
    
    pivot = daten[0]
    kleiner = []
    groesser = []
    gleich = []

    if isinstance(pivot, list):
        for element in daten:
            if isinstance(element, list):
                if element == pivot:
                    gleich.append(element)
                elif element < pivot:
                    kleiner.append(element)
                else:
                    groesser.append(element)
            else:
                if element < pivot:
                    kleiner.append(element)
                elif element > pivot:
                    groesser.append(element)
                else:
                    gleich.append(element)
    else:
        for element in daten:
            if isinstance(element, list):
                if element < pivot:
                    kleiner.append(element)
                elif element > pivot:
                    groesser.append(element)
                else:
                    gleich.append(element)
            else:
                if element == pivot:
                    gleich.append(element)
                elif element < pivot:
                    kleiner.append(element)
                else:
                    groesser.append(element)

    return quicksort_rek(kleiner) + gleich + quicksort_rek(groesser)


daten = [4, 2, 3, 1, 5, 1, 6, 3]
result = quicksort_rek(daten)
print(result)

