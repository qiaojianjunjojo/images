#!/usr/bin/env python
# -*- coding:utf-8 -*-


import tkinter as tk
win = tk.Tk()
win.title('yudanqu')
win.geometry("400x400+200+50")

def update(event):
    print(event.x,event.y)

lable = tk.Label(win,text = 'Move your mouse!',bg = 'yellow')
lable.pack()

lable.bind("<Enter>",update)
lable.bind("<Leave>",update)
win.mainloop()
