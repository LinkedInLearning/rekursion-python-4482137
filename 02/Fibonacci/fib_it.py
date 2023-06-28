def fib_it(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fbzl = [0, 1]
        while len(fbzl) < n:
            naechste_zahl = fbzl[-1] + fbzl[-2]
            fbzl.append(naechste_zahl)
        return fbzl


anzahl = int(input("Wie viele Fibonacci-Zahlen sollen berechnet werden? "))
fbzl = fib_it(anzahl)
print("Die Fibonacci-Zahlen lauten:")
print(fbzl)
