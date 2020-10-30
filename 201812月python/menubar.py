import tkinter as tk
from PIL import Image

window=tk.Tk()
window.geometry('200x200')
window.title('my window')
l = tk.Label(window,text = 'Empty',width = 200,bg='yellow')
l.pack()

counter=0
def do_job():
    global counter   
    l.configure(text = 'do'+str(counter))
    counter+=1
    
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar,tearoff = 0)
menubar.add_cascade(label = 'File',menu = filemenu)
filemenu.add_command(label='New',command = do_job)
filemenu.add_command(label='Open',command = do_job)
filemenu.add_command(label = 'Save',command = do_job)
filemenu.add_separator()
filemenu.add_command(label = 'Exit',command=window.quit)

helpmenu = tk.Menu(menubar,tearoff = 0)
menubar.add_cascade(label = 'Help',menu = helpmenu)
helpmenu.add_command(label = 'Help Index',command = do_job)
helpmenu.add_command(label = 'About..',command = do_job)
helpmenu.add_separator()
helpmenu.add_command(label = 'Exit',command=window.quit)

window.config(menu = menubar)



window.mainloop()


