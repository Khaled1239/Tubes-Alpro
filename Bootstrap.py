import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
from tkinter import PhotoImage
from DataBase import LD, SD
from Main import FRSearch, SNim, AddMahasiswa, EditData, RemoveData, SS, resource_path
import sys
import os
from PIL import Image, ImageTk
import numpy as np



if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
else:
    application_path = os.path.dirname(__file__)

os.environ['DEEPFACE_HOME'] = os.path.join(application_path, ".deepface")


Data = LD()

def FRS():
    FRSearch(Data)

def SNIM():
    SNim(Data)

def Add():
    AddMahasiswa(root,Data)

def Edit():
    EditData(root,Data)

def Remove():
    RemoveData(Data)

def Exit():
    SD(Data)
    root.destroy()

def ShowAfterSort():
    SS(Data)




root = ttk.Window(themename="cosmo")
root.title("Data Mahasiswa")
root.geometry("1280x720")

BGImg = Image.open(resource_path("UI/BG.png"))
BGImg = BGImg.resize((1280, 720))
BG_Photo = ImageTk.PhotoImage(BGImg)

BG_Label = ttk.Label(root, image=BG_Photo)
BG_Label.place(x=0, y=0, relwidth=1, relheight=1)

#label1 = tk.Label(root, text="~WELCOME~", font=("Helvetica", 30, "bold"))
#label1.pack(pady=(120, 0))
###############################################################################################
BImg1 = PhotoImage(file=resource_path("UI/CariDenganWajah.png"))
Button1 = tk.Button(root, image=BImg1, borderwidth=0, highlightthickness=0, command=FRS)
Button1.pack(pady=(240, 0))
##########################################################################################
BImg2 = PhotoImage(file=resource_path("UI/CariDenganNIM.png"))
Button2 = tk.Button(root, image=BImg2, borderwidth=0, highlightthickness=0, command=SNIM)
Button2.pack(pady=(10, 0))
##########################################################################################
BImg3 = PhotoImage(file=resource_path("UI/TambahMahasiswa.png"))
Button3 = tk.Button(root, image=BImg3, borderwidth=0, highlightthickness=0, command=Add)
Button3.pack(pady=(10, 0))
##########################################################################################
BImg4 = PhotoImage(file=resource_path("UI/EditMahasiswa.png"))
Button4 = tk.Button(root, image=BImg4, borderwidth=0, highlightthickness=0, command=Edit)
Button4.pack(pady=(10, 0))
##########################################################################################
BImg5 = PhotoImage(file=resource_path("UI/Remove.png"))
Button5 = tk.Button(root, image=BImg5, borderwidth=0, highlightthickness=0, command=Remove)
Button5.pack(pady=(10, 0))
##########################################################################################
BImg6 = PhotoImage(file=resource_path("UI/ShowSorted.png"))
Button6 = tk.Button(root, image=BImg6, borderwidth=0, highlightthickness=0, command=ShowAfterSort)
Button6.pack(pady=(10, 0))
##########################################################################################
BImg7 = PhotoImage(file=resource_path("UI/Exit.png"))
Button7 = tk.Button(root, image=BImg7, borderwidth=0, highlightthickness=0, command=Exit)
Button7.pack(pady=(10, 0))
##########################################################################################
root.mainloop()