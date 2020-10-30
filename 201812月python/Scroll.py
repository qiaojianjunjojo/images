#!/usr/bin/env python
# -*- coding:utf-8 -*-


import tkinter as tk
win = tk.Tk()
win.title('yudanqu')

scroll = tk.Scrollbar()

text = tk.Text(win,width = 30,height = 10)

scroll.pack(side = 'left',fill = 'y')
text.pack(side = 'left',fill = 'y')

scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)

text.pack()

str = '''盖闻天地之数，有十二万九千六百岁为一元。将一元分一元。将一元分物未生时。到此，天始有根。再五之会，而逐渐坚实。易曰：“大哉乾元！至哉坤元！万物资生，乃顺承天。”千四百岁，正当子、山、石、土谓之五形。故曰，地辟于丑。又经五千四百岁，丑会会，轻清上腾为十二会，乃子、丑、寅、卯、辰为十二会，乃子、丑、寅、卯、辰、巳、午、未、申、酉、戌、亥之十二支也。每会该一万八百岁。且就一日而论：子时得阳气，而丑'''

text.insert('insert', str)

win.mainloop()
