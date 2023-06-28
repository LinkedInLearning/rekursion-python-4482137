def merge_sort(daten):
    if len(daten) <= 1:
        return daten
    
    mitte = len(daten) // 2
    linke_haelfte = daten[:mitte]
    rechte_haelfte = daten[mitte:]
    
    linke_haelfte = merge_sort(linke_haelfte)
    rechte_haelfte = merge_sort(rechte_haelfte)
    
    return merge(linke_haelfte, rechte_haelfte)

def merge(links, rechts):
    merged = []
    i = j = 0
    
    while i < len(links) and j < len(rechts):
        if links[i] <= rechts[j]:
            merged.append(links[i])
            i += 1
        else:
            merged.append(rechts[j])
            j += 1
    
    merged.extend(links[i:])
    merged.extend(rechts[j:])
    
    return merged

daten = [5, 2, 8, 3, 1]
result = merge_sort(daten)
print(result)
