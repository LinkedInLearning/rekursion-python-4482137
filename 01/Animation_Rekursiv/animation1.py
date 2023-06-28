import tkinter as tk

def animate(rect, canvas):
    canvas.move(rect, 1, 1)
    canvas.update()

    if canvas.coords(rect)[2] < canvas.winfo_width():
        canvas.after(10, animate, rect, canvas)  # Rekursiver Aufruf

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()


rect = canvas.create_rectangle(0, 0, 50, 50, fill='red')
canvas.after(5000, animate, rect, canvas)

root.mainloop()
