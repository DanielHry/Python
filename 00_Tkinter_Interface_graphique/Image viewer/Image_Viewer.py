# -*- coding: utf-8 -*-
"""
Created on Sat May 9 2020

@author: Daniel Hryniewski
"""
from tkinter import *
from PIL import ImageTk,Image

def img_next(img_num):
    global my_label
    global btn_next
    global btn_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[img_num-1], bg = '#222831')
    
    btn_back = Button(root, text='<<', bg='#393e46', fg='#ffffff', command=lambda: img_back(img_num-1))
    btn_next = Button(root, text='>>', bg='#393e46', fg='#ffffff', command=lambda: img_next(img_num+1))
    status = Label(root, text=f"Image {img_num} of {len(image_list)}", bg = '#222831', fg='#ffffff')
    
    if img_num == len(image_list):
        btn_next = Button(root, text='>>', bg='#393e46', fg='#ffffff', command=lambda: img_next(1))
    
    my_label.grid(row=0, column=0, columnspan=3)
    btn_back.grid(row=1, column=0, rowspan=2)
    btn_next.grid(row=1, column=2, rowspan=2)
    status.grid(row=2, column=0, columnspan=3)
    

def img_back(img_num):
    global my_label
    global btn_next
    global btn_back
    
    my_label.grid_forget()
    my_label = Label(image=image_list[img_num-1], bg = '#222831')
    
    btn_back = Button(root, text='<<', bg='#393e46', fg='#ffffff', command=lambda: img_back(img_num-1))
    btn_next = Button(root, text='>>', bg='#393e46', fg='#ffffff', command=lambda: img_next(img_num+1))
    status = Label(root, text=f"Image {img_num} of {len(image_list)}", bg = '#222831', fg='#ffffff')
    
    if img_num == 1:
        btn_back = Button(root, text='<<', bg='#393e46', fg='#ffffff', command=lambda: img_next(len(image_list)))
    
    my_label.grid(row=0, column=0, columnspan=3)
    btn_back.grid(row=1, column=0, rowspan=2)
    btn_next.grid(row=1, column=2, rowspan=2) 
    status.grid(row=2, column=0, columnspan=3)


root = Tk()
root.title('Image Viewer')
root.iconbitmap('IV_icone.ico')
root.configure(bg = '#222831')


my_img1 = ImageTk.PhotoImage(Image.open('images/01.jpeg'))
my_img2 = ImageTk.PhotoImage(Image.open('images/02.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('images/03.jpg'))
my_img4 = ImageTk.PhotoImage(Image.open('images/04.jpg'))
my_img5 = ImageTk.PhotoImage(Image.open('images/05.jpg'))
my_img6 = ImageTk.PhotoImage(Image.open('images/06.jpg'))
my_img7 = ImageTk.PhotoImage(Image.open('images/07.jpg'))
my_img8 = ImageTk.PhotoImage(Image.open('images/08.png'))
my_img9 = ImageTk.PhotoImage(Image.open('images/09.jpeg'))

image_list = [my_img1, my_img2, my_img3, my_img4, my_img5, my_img6, my_img7, my_img8, my_img9]



my_label = Label(image = my_img1, bg = '#222831')
btn_back = Button(root, text='<<', bg='#393e46', fg='#ffffff', command=lambda: img_back(2))
btn_exit = Button(root, text='EXIT PROGRAM', bg='#393e46', fg='#ffffff', command=root.quit)
btn_next = Button(root, text='>>', bg='#393e46', fg='#ffffff', command=lambda: img_next(2))
status = Label(root, text=f"Image 1 of {len(image_list)}", bg = '#222831', fg='#ffffff')


my_label.grid(row=0, column=0, columnspan=3)
btn_back.grid(row=1, column=0, rowspan=2)
btn_exit.grid(row=1, column=1)
btn_next.grid(row=1, column=2, rowspan=2)
status.grid(row=2, column=0, columnspan=3)


root.mainloop()