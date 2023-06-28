# Funktion zum Lösen des Maze-Solving-Problems
def maze_loesen(labyrinth, start, ziel):
    # Überprüfen, ob der aktuelle Punkt außerhalb des Labyrinths liegt oder eine Wand ist
    def ist_gueltiger_punkt(punkt):
        i, j = punkt
        if i < 0 or i >= len(labyrinth) or j < 0 or j >= len(labyrinth[0]):
            return False
        return labyrinth[i][j] != '#'

    # Rekursive Funktion zur Exploration der möglichen Wege
    def explore(punkt, weg):
        i, j = punkt
        # Überprüfen, ob der Punkt außerhalb des Labyrinths liegt oder eine Wand ist
        if not ist_gueltiger_punkt(punkt):
            return False

        # Hinzufügen des aktuellen Punktes zum Weg
        weg.append(punkt)

        # Überprüfen, ob das Ziel erreicht wurde
        if punkt == ziel:
            return True

        # Markieren des aktuellen Punktes als besucht
        labyrinth[i][j] = '#'

        # Rekursiv in alle Richtungen weitergehen
        if explore((i - 1, j), weg) or explore((i + 1, j), weg) or explore((i, j - 1), weg) or explore((i, j + 1), weg):
            return True

        # Falls kein gültiger Pfad gefunden wurde, den aktuellen Punkt aus dem Weg entfernen
        weg.pop()

        return False

    # Startpunkt und Weg initialisieren
    weg = []
    if explore(start, weg):
        return weg
    else:
        return None


# Beispiel-Labyrinth mit einem gültigen Pfad
labyrinth_gueltig = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]
startpunkt_gueltig = (1, 1)
zielpunkt_gueltig = (5, 5)

# Beispiel-Labyrinth ohne gültigem Pfad
labyrinth_ungueltig = [
    ['#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#']
]
startpunkt_ungueltig = (1, 1)
zielpunkt_ungueltig = (4, 4)

# Versuch, das Labyrinth mit einem gültigen Pfad zu lösen
print("Ausgangslabyrinth\n")
for z in labyrinth_gueltig:
    print(z)
print("\n")
weg_gueltig = maze_loesen(
    labyrinth_gueltig, startpunkt_gueltig, zielpunkt_gueltig)
if weg_gueltig:
    print("Gültiger Pfad gefunden!")
    print("Wegbeschreibung:")
    for schritt, punkt in enumerate(weg_gueltig):
        print(f"Schritt {schritt + 1}: Gehe zu Punkt {punkt}")
else:
    print("Es wurde kein gültiger Pfad durch das Labyrinth gefunden.")

print("*"*20)

# Versuch, das Labyrinth ohne einen gültigen Pfad zu lösen
print("Ausgangslabyrinth\n")
for z in labyrinth_ungueltig:
    print(z)
print("\n")
weg_gueltig = maze_loesen(
    labyrinth_ungueltig, startpunkt_ungueltig, zielpunkt_ungueltig)
if weg_gueltig:
    print("Gültiger Pfad gefunden!")
    print("Wegbeschreibung:")
    for schritt, punkt in enumerate(weg_gueltig):
        print(f"Schritt {schritt + 1}: Gehe zu Punkt {punkt}")
else:
    print("Es wurde kein gültiger Pfad durch das Labyrinth gefunden.")
