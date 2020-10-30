#!/usr/bin/env python
# -*- coding:utf-8 -*-


import tkinter as tk
win = tk.Tk()
win.title('yudanqu')
win.geometry("400x400+200+50")


# <Key>  响应所有的按键（要有焦点）


def update(event):        
    print("event.char=", event.char)
  



lable = tk.Label(win,text = '*********!',bg = 'yellow')
lable.focus_set()
lable.pack()

win.bind("<Key>",update)


win.mainloop()
