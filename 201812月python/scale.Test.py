import tkinter as tk
window=tk.Tk()
window.geometry('200x200')

l=tk.Label(window,text='當前進度:',width = 20,bg = 'yellow')
l.pack()

def print_selection(v):
    l.configure(text = '當前進度：'+ v)
    
s=tk.Scale(window,label='',from_=0,to = 100, orient=tk.HORIZONTAL,
            length=200, showvalue=0, tickinterval=50, resolution=0.1,
           command=print_selection)
s.pack()

window.mainloop()


