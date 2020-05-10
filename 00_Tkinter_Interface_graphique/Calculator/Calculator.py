# -*- coding: utf-8 -*-
"""
Created on Thu May 7 2020

@author: Daniel Hryniewski
"""
from tkinter import *

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    
def btn_clear():
    e.delete(0, END)
    
def btn_add():
    f_num = e.get()
    global num1
    global math
    math = "addition"
    num1 = int(f_num)
    e.delete(0, END)
    
def btn_subtract():
    f_num = e.get()
    global num1
    global math
    math = "subtraction"
    num1 = int(f_num)
    e.delete(0, END)

def btn_multiply():
    f_num = e.get()
    global num1
    global math
    math = "multiplication"
    num1 = int(f_num)
    e.delete(0, END)

def btn_divide():
    f_num = e.get()
    global num1
    global math
    math = "division"
    num1 = int(f_num)
    e.delete(0, END)
    
def btn_equal():
    s_num = e.get()
    e.delete(0, END)
    if math == 'addition':
        e.insert(0, num1 + int(s_num))
    if math == 'subtraction':
        e.insert(0, num1 - int(s_num))
    if math == 'multiplication':
        e.insert(0, num1 * int(s_num))
    if math == 'division':
        e.insert(0, num1 / int(s_num))


clrwhite_01 = '#eeeeee'
clrblue_01 = '#14d5de'
clrblue_02 = '#00adb5'
clrdark_01 = '#222831'
clrdark_02 = '#393e46'
clrred_01 = '#A71F57'
clrred_02 = '#811844'


btnw=4
btnh=1
relief = "flat"
fontButton = ('CourierNew', 18)
gridpady = 8




root = Tk()
root.geometry("330x315")
root.configure(bg = clrdark_01)
root.title("Simple Calculator")
root.bind('KeyPress-KP_1', lambda: button_click(1))
root.iconbitmap('calc.ico')


e = Entry(root, justify='right', width = 20, borderwidth=5, font=('CourierNew', 20), bg=clrdark_02, fg=clrwhite_01)

button_1 = Button(root, text='1', font=fontButton, width=btnw, height=btnh, bg=clrblue_01 ,activebackground=clrblue_02, command=lambda: button_click(1))
button_2 = Button(root, text='2', font=fontButton, width=btnw, height=btnh, bg=clrblue_01 ,activebackground=clrblue_02, command=lambda: button_click(2))
button_3 = Button(root, text='3', font=fontButton, width=btnw, height=btnh, bg=clrblue_01 ,activebackground=clrblue_02, command=lambda: button_click(3))
button_4 = Button(root, text='4', font=fontButton, width=btnw, height=btnh, bg=clrblue_01 ,activebackground=clrblue_02, command=lambda: button_click(4))
button_5 = Button(root, text='5', font=fontButton, width=btnw, height=btnh, bg=clrblue_01 ,activebackground=clrblue_02, command=lambda: button_click(5))
button_6 = Button(root, text='6', font=fontButton, width=btnw, height=btnh, bg=clrblue_01 ,activebackground=clrblue_02, command=lambda: button_click(6))
button_7 = Button(root, text='7', font=fontButton, width=btnw, height=btnh, bg=clrblue_01 ,activebackground=clrblue_02, command=lambda: button_click(7))
button_8 = Button(root, text='8', font=fontButton, width=btnw, height=btnh, bg=clrblue_01 ,activebackground=clrblue_02, command=lambda: button_click(8))
button_9 = Button(root, text='9', font=fontButton, width=btnw, height=btnh, bg=clrblue_01 ,activebackground=clrblue_02, command=lambda: button_click(9))
button_0 = Button(root, text='0', font=fontButton, width=btnw, height=btnh, bg=clrblue_01 ,activebackground=clrblue_02, command=lambda: button_click(0))

button_add      = Button(root, text='+',     font=fontButton, width=btnw, height=btnh, bg=clrblue_02, activebackground=clrblue_01, command=btn_add)
button_subtract = Button(root, text='-',     font=fontButton, width=btnw, height=btnh, bg=clrblue_02, activebackground=clrblue_01, command=btn_subtract)
button_multiply = Button(root, text='*',     font=fontButton, width=btnw, height=btnh, bg=clrblue_02, activebackground=clrblue_01, command=btn_multiply)
button_divide   = Button(root, text='/',     font=fontButton, width=btnw, height=btnh, bg=clrblue_02, activebackground=clrblue_01, command=btn_divide)
button_equal    = Button(root, text='=',     font=fontButton, width=btnw, height=btnh, bg=clrblue_02, activebackground=clrblue_01, command=btn_equal)
button_clear    = Button(root, text='Clear', font=fontButton, width=btnw, height=btnh, bg=clrred_01, activebackground=clrred_02, command=btn_clear)



e.grid(row=0, column=0, columnspan=4, padx=10,pady=10)

button_1.grid(row=3, column=0, pady=gridpady)
button_2.grid(row=3, column=1, pady=gridpady)
button_3.grid(row=3, column=2, pady=gridpady)
button_4.grid(row=2, column=0, pady=gridpady)
button_5.grid(row=2, column=1, pady=gridpady)
button_6.grid(row=2, column=2, pady=gridpady)
button_7.grid(row=1, column=0, pady=gridpady)
button_8.grid(row=1, column=1, pady=gridpady)
button_9.grid(row=1, column=2, pady=gridpady)
button_0.grid(row=4, column=1, pady=gridpady)

button_add.grid(row=1, column=3, pady=gridpady)
button_subtract.grid(row=2, column=3, pady=gridpady)
button_multiply.grid(row=3, column=3, pady=gridpady)
button_divide.grid(row=4, column=3, pady=gridpady)
button_equal.grid(row=4, column=2, pady=gridpady)
button_clear.grid(row=4, column=0, pady=gridpady)



root.mainloop()