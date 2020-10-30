import tkinter as tk
from tkinter import messagebox
window = tk.Tk()
window.title('my test window')
window.geometry('200x200')

ent = tk.Entry(window,show = '*')
ent.pack()

def func1():
    messagebox.showinfo(title='Hi', message='hahahaha')
def func2():
    messagebox.showwarning(title='Hi', message='hahahaha')
def func3():
    messagebox.showerror(title='Hi', message='hahahaha')
def func4():
    messagebox.askyesno(title='Hi', message='hahahaha')

bu1 = tk.Button(window,text = 'message',command = func1)
bu1.pack()
bu2 = tk.Button(window,text = 'warning',command = func2)
bu2.pack()
bu3 = tk.Button(window,text = 'Error',command = func3)
bu3.pack()
bu4 = tk.Button(window,text = 'Askquestion',command = func4)
bu4.pack()



window.mainloop()
