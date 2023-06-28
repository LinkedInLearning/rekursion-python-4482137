import tkinter as tk

def animate():
    global rect,canvas,x,y

    canvas.move(rect, x, y)
    canvas.update()

    if canvas.coords(rect)[2] < canvas.winfo_width():
        canvas.after(10, animate)  # Selbstaufruf

root = tk.Tk()
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

rect = canvas.create_rectangle(0, 0, 50, 50, fill='red')
x=1
y=1
canvas.after(4000, animate)

root.mainloop()
