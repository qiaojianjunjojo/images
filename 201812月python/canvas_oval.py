import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title('my test window')
window.geometry('1200x800')

x = 360
y = 160
top = y - 30
bottom = y - 30

canvas = tk.Canvas(window,width = 500,height = 600,bg = 'white')

for i in range(20):
    oval = canvas.create_oval(250 - top,250 - bottom,250 + top,250 + bottom)
    top-=5
    bottom+=5
    

canvas.pack()



window.mainloop()
