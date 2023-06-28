i = 0
def zaehle():
    global i
    i += 1
    print(i)
    if i < 10:
      zaehle()
zaehle()