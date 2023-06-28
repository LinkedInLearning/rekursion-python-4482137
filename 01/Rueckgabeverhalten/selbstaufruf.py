def zaehle(i):
    i += 1
    if i < 10:
        zaehle(i)
    print(i)
    return(i)

print("Rückgabewert:",zaehle(0))
