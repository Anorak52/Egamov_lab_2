import wm_lab_calc
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import tkinter.ttk as ttk
import tkinter as tk
import time, threading
import math
from matplotlib import pyplot as plt

main = Tk()
main.title("Численное методы lab2")
main.geometry("300x350")

label1 = Label(text = "Длина", font = "Arial 11")
label1.grid(row=0, column=0)
label2 = Label(text = "Время", font = "Arial 11")
label2.grid(row=1, column=0)
label3 = Label(text = "tau", font = "Arial 11")
label3.grid(row=2, column=0)
label4 = Label(text = "h", font = "Arial 11")
label4.grid(row=3, column=0)
label5 = Label(text = "b₀ = ", font = "Arial 11")
label5.grid(row=4, column=0)
label6 = Label(text = "b1 = ", font = "Arial 11")
label6.grid(row=5, column=0)
label7 = Label(text = "b2 = ", font = "Arial 11")
label7.grid(row=6, column=0)
label8 = Label(text = "Фи0 = ", font = "Arial 11")
label8.grid(row=7, column=0)
label9 = Label(text = "Фи1 = ", font = "Arial 11")
label9.grid(row=8, column=0)

_l=DoubleVar()
_t=DoubleVar()
_h1=DoubleVar()
_h2=DoubleVar()
_b0=DoubleVar()
_b1=DoubleVar()
_b2=DoubleVar()
_f0=DoubleVar()
_f1=DoubleVar()

entry1 = Entry(textvariable = _l, font = "Arial 11")
entry1.grid(row=0, column=1, padx=5, pady=5)
entry2 = Entry(textvariable = _t, font = "Arial 11")
entry2.grid(row=1, column=1, padx=5, pady=5)
entry3 = Entry(textvariable = _h1, font = "Arial 11")
entry3.grid(row=2, column=1, padx=5, pady=5)
entry4 = Entry(textvariable = _h2, font = "Arial 11")
entry4.grid(row=3, column=1, padx=5, pady=5)
entry5 = Entry(textvariable = _b0, font = "Arial 11")
entry5.grid(row=4, column=1, padx=5, pady=5)
entry6 = Entry(textvariable = _b1, font = "Arial 11")
entry6.grid(row=5, column=1, padx=5, pady=5)
entry7 = Entry(textvariable = _b2, font = "Arial 11")
entry7.grid(row=6, column=1, padx=5, pady=5)
entry8 = Entry(textvariable = _f0, font = "Arial 11")
entry8.grid(row=7, column=1, padx=5, pady=5)
entry9 = Entry(textvariable = _f1, font = "Arial 11")
entry9.grid(row=8, column=1, padx=5, pady=5)

entry1.delete(0, END)
entry1.insert(0, "20.0")
entry2.delete(0, END)
entry2.insert(0, "10.0")
entry3.delete(0, END)
entry3.insert(0, "0.01")
entry4.delete(0, END)
entry4.insert(0, "0.2")
entry5.delete(0, END)
entry5.insert(0, "0.001")
entry6.delete(0, END)
entry6.insert(0, "0.03")
entry7.delete(0, END)
entry7.insert(0, "0.0")
entry8.delete(0, END)
entry8.insert(0, "0.0")
entry9.delete(0, END)
entry9.insert(0, "0.0")

btn = Button(main, text= "График", command = lambda: wm_lab_calc.main(float(_l.get()), 
float(_t.get()), float(_h1.get()), float(_h2.get()), float(_b0.get()), float(_b1.get()), 
float(_b2.get()), float(_f0.get()), float(_f1.get())))
btn.grid(row=10,column=0)

main.mainloop()
