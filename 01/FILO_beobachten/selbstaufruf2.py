i = 0
def zaehle():
    global i
    i += 1
   
    if i < 10:
      zaehle()
    print(i)
zaehle()