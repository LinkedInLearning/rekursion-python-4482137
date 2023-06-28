def hanoi(n, start, ziel, hilfsstab):
    if n == 1:
        print("Bewege Scheibe 1 von Stab", start, "nach Stab", ziel)
        return

    hanoi(n-1, start, hilfsstab, ziel)
    print("Bewege Scheibe", n, "von Stab", start, "nach Stab", ziel)
    hanoi(n-1, hilfsstab, ziel, start)

hanoi(3, 1, 3, 2)
