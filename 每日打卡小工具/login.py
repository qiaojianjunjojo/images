#coding = "utf-8"

import tkinter as tk
import  tkinter.messagebox
import  pickle
import pandas as pd
import datetime,os


window = tk.Tk()
window.title('login')
window.geometry('400x300')
window.resizable(0,0)
# 登陆界面
tk.Label(window, text='账户：').place(x=100,y=100)
tk.Label(window, text='密码：').place(x=100, y=140)

var_usr_name = tk.StringVar()
enter_usr_name = tk.Entry(window, textvariable=var_usr_name)
enter_usr_name.place(x=160, y=100)

var_usr_pwd = tk.StringVar()
enter_usr_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
enter_usr_pwd.place(x=160, y=140)

def write_excel():
    user = var_usr_name.get() #用户
    cur_date = datetime.datetime.now().strftime('%Y%m%d') # '20200706'
    status = "OK"
    if not os.path.exists('./dailycheck.csv'):
        df = pd.DataFrame(columns=['date','name',"status"])
        df.to_csv("dailycheck.csv",index=False,encoding='utf_8_sig')
    df = pd.DataFrame([[cur_date,user,status]],columns=['date','name',"status"])
    df.to_csv('dailycheck.csv',mode='a',header=False,index=False,encoding='utf_8_sig')
    tk.messagebox.showinfo(message='打卡成功！')
    top.destroy()
    window.wm_deiconify()


def cancel2():
    top.destroy()
    window.wm_deiconify()

def daily_check():
    window.withdraw()
    global top
    top = tk.Toplevel()
    top.title = 'leetcode每日打卡'
    top.geometry('400x300')
    top.resizable(0,0)
    bt = tk.Button(top, text='今日打卡',bg = 'green',command= write_excel).place(x=180,y=150)
    bt2 = tk.Button(top,text = 'exit',command = cancel2).place(x = 250,y = 150)

#登陆
def usr_log_in():
    #输入框内容
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    try:
        with open('usr_info.pickle', 'rb') as usr_file:
            usrs_info=pickle.load(usr_file)
    except:
        with open('usr_info.pickle', 'wb') as usr_file:
            usrs_info={'admin':'admin'}
            pickle.dump(usrs_info, usr_file)

    # 判断
    if usr_name in usrs_info:
        if usr_pwd == usrs_info[usr_name]:
            tk.messagebox.showinfo(title='Welcome', message='###'+usr_name)
            #进入打卡界面
            daily_check()
        else:
            tk.messagebox.showerror(message='ERROR!密码错误！')
    # 用户名密码不能为空
    elif usr_name == '' or usr_pwd == '':
        tk.messagebox.showerror(message='用户名不能为空！')
    else:
        tk.messagebox.showwarning(message='用户不存在！请先注册！')

def usr_sign_quit():
    window.destroy()

def cancel():
    window_sign_up.destroy()
    window.wm_deiconify()

def usr_sign_up():
    window.withdraw()
    def signtowcg():
        NewName = new_name.get()
        NewPwd = new_pwd.get()
        ConfirPwd = pwd_comfirm.get()
        try:
            with open('usr_info.pickle', 'rb') as usr_file:
                exist_usr_info = pickle.load(usr_file)
        except FileNotFoundError:
            exist_usr_info = {}
        if NewName in exist_usr_info:
            tk.messagebox.showerror(message='用户名存在！')
        elif NewName == '' and NewPwd == '':
            tk.messagebox.showerror(message='用户名和密码不能为空！')
        elif NewPwd != ConfirPwd:
            tk.messagebox.showerror(message='密码前后不一致！')
        else:
            exist_usr_info[NewName] = NewPwd
            with open('usr_info.pickle', 'wb') as usr_file:
                pickle.dump(exist_usr_info, usr_file)
                tk.messagebox.showinfo(message='注册成功！')
                window_sign_up.destroy()
                window.wm_deiconify()

    # 新建注册窗口
    global window_sign_up
    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('400x300')
    window_sign_up.title('sign_up')

    # 注册编辑框
    new_name = tk.StringVar()
    new_pwd = tk.StringVar()
    pwd_comfirm = tk.StringVar()

    tk.Label(window_sign_up, text='账户名：').place(x=90,y=50)
    tk.Entry(window_sign_up, textvariable=new_name).place(x=160, y=50)

    tk.Label(window_sign_up, text='密码：').place(x=90,y=100)
    tk.Entry(window_sign_up, textvariable=new_pwd, show='*').place(x=160, y=100)

    tk.Label(window_sign_up, text='确认密码：').place(x=90, y=150)
    tk.Entry(window_sign_up, textvariable=pwd_comfirm, show='*').place(x=160, y=150)
#确认注册
    bt_confirm = tk.Button(window_sign_up, text='确定', command=signtowcg).place(x=150,y=220)
    bt_cancel = tk.Button(window_sign_up, text='取消', command=cancel).place(x=220,y=220)

#登录 注册按钮
bt_login = tk.Button(window,text='登录',command=usr_log_in)
bt_login.place(x=120,y=230)

bt_signup = tk.Button(window,text='注册',command=usr_sign_up)
bt_signup.place(x=190,y=230)

bt_logquit = tk.Button(window,text='退出',command=usr_sign_quit)
bt_logquit.place(x=260,y=230)

window.mainloop()