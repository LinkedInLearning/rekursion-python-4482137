def fib_rek(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fib_rek(n - 1) + fib_rek(n - 2)


def erstelle_fib_liste(fbzl, i):
    
    if i < 10:
        
        fbzl.append(fib_rek(i))
        i += 1
        erstelle_fib_liste(fbzl, i)
    return fbzl


print(erstelle_fib_liste([],0))