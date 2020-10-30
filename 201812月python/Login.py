import tkinter as tk
import pickle
from tkinter import messagebox
window = tk.Tk()
window.geometry('300x200')
window.title('Login')

user_l = tk.Label(window,text = 'User name: ')
user_l.place(x=10,y=10)
pwd_l = tk.Label(window,text = 'Password: ')
pwd_l.place(x=10,y=30)


def sign_up():
    def checkup():
        nn=new_name.get()
        np=new_pwd.get()
        np2=new_pwd2.get()
        with open('usrs_info.pickle','rb') as usr_file:
            exist_usr = pickle.load(usr_file)

        if np!=np2:
            tk.messagebox.showerror('Error','Password and confirm password must be the same!')
        elif nn in exist_usr:
            tk.messagebox.showerror('Error','The user has already signed up!')
        else:
            exist_usr[nn]=np
            with open('usrs_info.pickle','wb') as usr_file:
                pickle.dump(exist_usr,usr_file)

            tk.messagebox.showinfo('Welcome','You have successfully signed up!')
            w2.destroy()
        
        
    w2=tk.Toplevel(window)
    w2.geometry('300x200')
    w2.title('Sign up Window')
    w2.resizable(0,0)
    new_name=tk.StringVar()
    new_pwd=tk.StringVar()
    new_pwd2=tk.StringVar()

    tk.Label(w2,text='UserName').place(x=10,y=10)
    tk.Label(w2,text='Password').place(x=10,y=30)
    tk.Label(w2,text='Confirm Password').place(x=10,y=50)
    entry_name = tk.Entry(w2,textvariable = new_name,show = None)
    entry_name.place(x=150,y=10)
    entry_pwd = tk.Entry(w2,textvariable = new_pwd,show = '*')
    entry_pwd.place(x=150,y=30)
    entry_pwd2 = tk.Entry(w2,textvariable = new_pwd2,show = '*')
    entry_pwd2.place(x=150,y=50)

    sign_b = tk.Button(w2,text = 'Sign up',command = checkup).place(x=150,y=70)

def login():
    username = uservar.get()
    userpwd = pwdvar.get()
    try:
        with open('usrs_info.pickle','rb') as usr_file:
            usr_info = pickle.load(usr_file)
            if username  in usr_info:
                if userpwd == usr_info[username]:
                    tk.messagebox.showinfo(title ='Welcome',message = '登陸成功！')
                else :
                    tk.messagebox.showinfo(title ='Welcome',message = '用戶名或者密碼錯誤，請重試！')
 
            else:
                is_sign_up = tk.messagebox.askyesno("Welcome","該用戶尚未註冊，現在開始註冊？")
                if is_sign_up :
                    sign_up()
            
    except FileNotFoundError:
        with open('usrs_info.pickle','wb') as usr_file:
            usrs_info ={'admin':'admin'}
            pickle.dump(usrs_info,usr_file)

    
       
            
def signup():
    pass
uservar = tk.StringVar()
uservar.set('jianjun.qiao@qq.com')
pwdvar =tk.StringVar()
user_entry = tk.Entry(window,textvariable=uservar,show=None)
user_entry.place(x=150,y=10)
pwd_entry = tk.Entry(window,textvariable = pwdvar,show = '*')
pwd_entry.place(x=150,y=30)
b1=tk.Button(window,text ='Login',bg = 'blue',command = login)
b1.place(x=100,y=80)
b2=tk.Button(window,text ='Sign up',bg = 'blue',command = sign_up)
b2.place(x=150,y=80)

window.resizable(0,0)
window.mainloop()
