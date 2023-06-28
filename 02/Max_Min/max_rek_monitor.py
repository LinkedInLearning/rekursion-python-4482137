monitor = 0
def maximum_berechnen(zahlen):
    global monitor
    monitor += 1
    if len(zahlen) == 0:
        return None
    if len(zahlen) == 1:
        return zahlen[0]
    # Teile die Liste in zwei Hälften
    mitte = len(zahlen) // 2
    # Rekursiv das Maximum in den beiden Hälften suchen
    maximum_links = maximum_berechnen(zahlen[:mitte])
    maximum_rechts = maximum_berechnen(zahlen[mitte:])

    if maximum_links is None:
        return maximum_rechts
    if maximum_rechts is None:
        return maximum_links
    # Vergleiche die beiden Maximum-Werte und gib das größere zurück
    return maximum_links if maximum_links > maximum_rechts else maximum_rechts


# Beispielaufruf
zahlen = [4, 9, 2, 7, 5,11,31,42,12,1,66,17]
max_wert = maximum_berechnen(zahlen)
print("Das Maximum der Zahlen ist:", max_wert)
print("Anzahl der Überprüfungen:", monitor)
