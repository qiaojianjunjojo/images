#coding = 'utf-8'
import tkinter
import tkinter.messagebox 
import tkinter.scrolledtext
from pypinyin.phrases_dict import phrases_dict
from pypinyin.pinyin_dict import pinyin_dict

root = tkinter.Tk()
root.geometry('700x400+200+200')
root.title('汉语拼音学习机')
root.resizable(0, 0)

(tkinter.Label(root,
               text='输入要查询的内容：',
               anchor='e',
               font=('microsoft yahel', 16)).place(x=10,
                                                   y=10,
                                                   width=200,
                                                   height=40))
entrysearch = tkinter.Entry(root, font=('microsoft yahel', 16))
entrysearch.place(x=220, y=10, width=180, height=40)
search_type = tkinter.IntVar(root, value=0)
radioPinyin = tkinter.Radiobutton(root,
                                  text='查单字拼音',
                                  variable=search_type,
                                  value=0)
radioPinyin.place(x=410, y=20, width=80, height=20)
radioPhrase = tkinter.Radiobutton(root,
                                  text='查词组',
                                  variable=search_type,
                                  value=1)
radioPhrase.place(x=500, y=20, width=60, height=20)
include_pinyin = tkinter.BooleanVar(root, value=False)
checkbuttonInclude = tkinter.Checkbutton(root,
                                         variable=include_pinyin,
                                         text='包含词组拼音',
                                         onvalue=True,
                                         offvalue=False)
checkbuttonInclude.place(x=580, y=20, width=100, height=20)


def search():
    textContent.delete('0.0',tkinter.END)
    user_input = entrysearch.get().strip()
    if not user_input:
        tkinter.messagebox.showinfo('提示','查询内容不能为空')
        return 
    if search_type.get()==0:
        if len(user_input)>1:
            tkinter.messagebox.showinfo('提示','只能查单个字的读音')
            return
        for num,pinyin in pinyin_dict.items():
            if chr(num) == user_input:
                textContent.insert(tkinter.INSERT,f'"{user_input}"的拼音有：\n{pinyin}')
                return 

        else:
            tkinter.messagebox.showinfo('sorry','你太厉害了，我都不认识这个字！')

    if search_type.get()==1:
        flag = False
        for phrase,pinyin in phrases_dict.items():
            #if all(map(phrase.count,user_input)):
            if phrase.count(user_input):
                if include_pinyin.get():
                    msg = f'{phrase}:{pinyin}\n'
                else:
                    msg = f'{phrase}\n'
                textContent.insert(tkinter.INSERT,msg)
                flag = True
        if not flag:
            tkinter.messagebox.showinfo('sorry','没有找到相关词组！')
(tkinter.Button(root, text='查询', command=search,
                font=('microsoft yahel', 16)).place(x=10,
                                                    y=60,
                                                    width=60,
                                                    height=40))
textContent = tkinter.scrolledtext.ScrolledText(root,
                                                font=('microsoft yahel', 16))
textContent.place(x=10, y=110, width=680, height=280)

root.mainloop()