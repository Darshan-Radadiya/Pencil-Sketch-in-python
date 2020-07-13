import os
import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
from tkinter.filedialog import askopenfilename
import cv2
import sys

root = tk.Tk(className='Photo Editor')
root.geometry("700x400+0+0")

heading = Label(root, text="...Pencil Sketch...", font=("bold"), fg="steelblue").place(x=270,y=20)

def openfile1():
    global filename
    filename = askopenfilename()

def pencil():
    image = cv2.imread(filename)
    grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    grayImageInv = 255 - grayImage
    grayImageInv = cv2.GaussianBlur(grayImageInv, (21,21),0)
    global output
    output = cv2.divide(grayImage,255-grayImageInv, scale=256.0)
    #cv2.namedWindow("image",cv2.WINDOW_NORMAL)
    #cv2.namedWindow("pecilsketch",cv2.WINDOW_NORMAL)
    #cv2.imshow("image", image)
    cv2.imshow("pencilsketch",output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
def sav():
    y = datetime.datetime.now()
    Z = y.strftime("%H") + y.strftime("%M") + y.strftime("%S") + ".jpg"
    cv2.imwrite(Z,output)
    msg = Message(root, text = "Picture Saved Successfully",font = (10) ,foreground = 'Green',bg = 'lightgreen',aspect = 480).place(x=180,y=250)

b2 = Button(root, text='Open file',activebackground = 'Blue', activeforeground = 'lightblue',cursor='plus',padx=15,pady=5,width=10,command=openfile1).place(x=290, y=100)
b3 = Button(root, text='Convert', activebackground = 'Blue',activeforeground = 'lightblue',padx=15,pady=5,cursor='star',width=10,command=pencil).place(x=290, y=150)
b4 = Button(root, text='Save', activebackground = 'Blue',activeforeground = 'lightblue',padx=15,pady=5,cursor='heart',width=10,command=sav).place(x=290, y=200)
root.mainloop()


