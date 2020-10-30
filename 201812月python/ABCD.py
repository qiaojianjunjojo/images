import tkinter as tk
window=tk.Tk()
window.geometry('200x200')

l=tk.Label(window,text='請選擇你的答案:',width = 20,bg = 'yellow')
l.pack()

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
def select():
    if((var1.get()==1)&(var2.get()==0)&(var3.get()==0)&(var4.get()==0)):
        l.configure(text = '我選擇A')
    elif((var2.get()==1)&(var1.get()==0)&(var3.get()==0)&(var4.get()==0)):
         l.configure(text = '我選擇B')
    elif((var3.get()==1)&(var1.get()==0)&(var2.get()==0)&(var4.get()==0)):
         l.configure(text = '我選擇C')
    elif((var4.get()==1)&(var1.get()==0)&(var2.get()==0)&(var3.get()==0)):
         l.configure(text = '我選擇D')
    else:
         l.configure(text = '請不要多選!')
        
  


c1=tk.Checkbutton(window,text = 'A',variable = var1,onvalue = 1,offvalue = 0,
                  command = select)
c1.pack()

c2=tk.Checkbutton(window,text = 'B',variable = var2,onvalue = 1,offvalue = 0,
                  command = select)
c2.pack()
c3=tk.Checkbutton(window,text = 'C',variable = var3,onvalue = 1,offvalue = 0,
                  command = select)
c3.pack()
c4=tk.Checkbutton(window,text = 'D',variable = var4,onvalue = 1,offvalue = 0,
                  command = select)
c4.pack()
window.mainloop()


