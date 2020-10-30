import tkinter as tk
window=tk.Tk()
window.geometry('200x200')

l=tk.Label(window,width = 20,bg='yellow',text = 'empty')
l.pack()

def select_option():
    l.configure(text = 'you have selected ' + var.get())
var = tk.StringVar()
r1=tk.Radiobutton(window,text='Option A',variable = var,value = 'A',
                  command = select_option)

r1.pack()
r2=tk.Radiobutton(window,text='Option B',variable = var,value = 'B',
                  command = select_option)

r2.pack()
r3=tk.Radiobutton(window,text='Option C',variable = var,value = 'C',
                  command = select_option)

r3.pack()
window.mainloop()
