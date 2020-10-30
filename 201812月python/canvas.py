import tkinter as tk
from PIL import Image

window=tk.Tk()
window.geometry('200x200')

canvas = tk.Canvas(window,width = 200,height = 100,bg = 'yellow')
#canvas.pack()
canvas.grid()
image_file = Image.open('desk.jpg')
#image = canvas.create_image(10, 10, anchor='nw', image=image_file)

x0, y0, x1, y1= 50, 50, 110, 80
line = canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0, y0, x1, y1, fill='red')  #创建一个圆，填充色为`red`红色
arc = canvas.create_arc(x0+30, y0+30, x1+30, y1+30, start=0, extent=90)  #创建一个扇形
rect = canvas.create_rectangle(100, 30, 100+30, 30+20)   #创建一个矩形

def move_it1():
    canvas.move(rect, 0, -2)
    
def move_it2():
    canvas.move(rect, 0, 2)

def move_it3():
    canvas.move(rect, -2, 0)

def move_it4():
    canvas.move(rect, 2, 0)
    
b1 = tk.Button(window,text = 'MoveUp',command = move_it1)
#b1.pack()
b1.grid(column=0,row=3)
b2 = tk.Button(window,text = 'MoveDown',command = move_it2)
#b2.pack()
b2.grid(column=10,row=3)
b3 = tk.Button(window,text = 'MoveLeft',command = move_it3)
#b3.pack()
b3.grid(column=10,row=2)
b4 = tk.Button(window,text = 'MoveRight',command = move_it4)
#b4.pack()
b4.grid(column=10,row=4)
window.mainloop()


