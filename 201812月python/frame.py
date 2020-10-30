import tkinter as tk

window=tk.Tk()
window.geometry('200x200')
window.title('my window')
l = tk.Label(window,text = 'on the window',width = 200,bg='yellow')
l.pack()

frm = tk.Frame(window)
frm.pack()

frml = tk.Frame(frm)
frmr = tk.Frame(frm)
frml.pack(side = 'left')
frmr.pack(side = 'right')

tk.Label(frml,text = 'on the frm l1',bg = 'red').pack()
tk.Label(frml,text = 'on the frm l2',bg = 'blue').pack()
tk.Label(frmr,text = 'on the frm r1',bg = 'green').pack()

frm2=tk.Frame(window)
frm2.pack()
frm3 =tk.Frame(window)
frm3.pack(side = 'bottom')
redb = tk.Button(frm2,text = 'Red',fg = 'red')
redb.pack(side = 'left')
greenb = tk.Button(frm2,text = 'green',fg = 'green')
greenb.pack(side = 'left')
blueb = tk.Button(frm2,text = 'blue',fg = 'blue')
blueb.pack(side = 'left')

blackb = tk.Button(frm3,text = 'black',fg = 'black')
blackb.pack(side = 'bottom')

window.resizable(0,0)
window.mainloop()


