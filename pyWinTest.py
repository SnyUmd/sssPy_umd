# coding: UTF-8
import tkinter
from tkinter import filedialog

def btn_Click():
    typ = [('Excelファイル','*.xlsx')]
    dir = 'D:\_git\Python'
    fle = filedialog.askopenfilename(filetypes = typ, initialdir = dir)
    print(fle)



# Tkクラス生成
frm = tkinter.Tk()
# 画面サイズ
frm.geometry('200x100')
# 画面タイトル
frm.title('サンプル画面')

btn = tkinter.Button(frm, text='ボタン', width=10, height=1, command=btn_Click )
btn.place(x=100, y=10)

txb = tkinter

# 画面をそのまま表示
frm.mainloop()
