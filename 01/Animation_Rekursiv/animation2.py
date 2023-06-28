import tkinter as tk

def animate_diameter(rectangle, rot, gruen, blau):
    if rot > 254:
        return
    rot_hex= str(hex(rot) )[2:]
    if len(rot_hex)==1:
        rot_hex= "0"+rot_hex
    gruen_hex= str(hex(gruen % 255) )[2:]
    if len(gruen_hex)==1:
        gruen_hex= "0"+gruen_hex
    blau_hex= str(hex(blau % 255) )[2:]
    if len(blau_hex)==1:
        blau_hex= "0"+blau_hex
    #print(blau_hex)
    canvas.itemconfig(rectangle, fill="#"+rot_hex+gruen_hex+ blau_hex)
    canvas.after(15, animate_diameter, rectangle, rot+1,gruen+2,blau+3)

# Erstelle das Tkinter-Fenster
window = tk.Tk()
window.title("Kreis Animation")
window.geometry("400x400")

# Erstelle die Canvas-Leinwand
canvas = tk.Canvas(window, width=300, height=300)
canvas.pack()

# Zeichne das rote Kreisrechteck
rectangle = canvas.create_oval(50, 50, 150, 150, outline="red", fill="#000000")
rot = 0
gruen = 0
blau = 0
# Starte die Animation
canvas.after(5000, animate_diameter, rectangle, rot,gruen,blau)

# Starte die Tkinter-Schleife
window.mainloop()
