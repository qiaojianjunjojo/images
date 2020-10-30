import tkinter as tk
window = tk.Tk()
window.title('my window')
window.geometry('200x200')

ent = tk.Entry(window,show = None)
ent.pack()

def insert_point():
    var = ent.get()
    t.insert('insert',var)
    
def insert_end():
    var = ent.get()
    t.insert('end',var)

bu1 = tk.Button(window,text = 'insert point',command = insert_point)
bu1.pack()
bu2 = tk.Button(window,text = 'insert end',command = insert_end)
bu2.pack()

t = tk.Text(window,height = 2)
t.pack()

window.mainloop()
