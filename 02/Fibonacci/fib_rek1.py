def fib_rek(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fib_rek(n - 1) + fib_rek(n - 2)


i = 0
while i < 10:
    print(fib_rek(i))
    i += 1
fbz1 = []
i = 0
while i < 10:
    fbz1.append(fib_rek(i))
    i += 1
print(fbz1)
