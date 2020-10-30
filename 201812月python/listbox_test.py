import tkinter as tk
import sys

window = tk.Tk()
window.title('my tkinter')
window.geometry("200x200")
var = tk.StringVar()
l=tk.Label(window,bg = 'yellow',width = 40,height= 2,
            text = 'your choice will be show here!')
l.pack()
def select_option():    
    var2 = lb.get(lb.curselection())    
    l.configure(text=var2)
    

    
b=tk.Button(window,text = 'select this one!',bg = 'blue',
            command = select_option,width = 25)
b.pack()
e=tk.Entry(window,width = 20,show = '*')
e.pack()

def insert_password():
    var4=e.get()
    lb.insert('end',var4)
    
b2=tk.Button(window,text='ADD password',bg='red',command = insert_password)
b2.pack()

var3 = tk.StringVar()
var3.set(('a','b','c','d'))
lb=tk.Listbox(window,listvariable = var3)
li = ['LGP_1', 'LGP_2', 'LGP_3']
for item in li:
    lb.insert("end",item)
lb.pack()


window.mainloop()
    






