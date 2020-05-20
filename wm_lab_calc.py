#Copyright Brazhnikov Eugene 2020

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

global yellow, _x, a, canvas

def continue_():
    a.plot(_x, green, label = "Final temp A", color='yellow')
    a.legend()
    canvas.draw()

def method(A, B, C, F):
    size = len(F)
    sizeM = size - 1
    i = 1
    a = [1] * sizeM
    b = [1] * sizeM
    x = [1] * size
    a[0] = -C[0] / B[0]
    b[0] = F[0] / B[0]
    while (i < sizeM):
        a[i] = -C[i] / (A[i] * a[i - 1] + B[i])
        b[i] = (F[i] - A[i] * b[i - 1]) / (A[i] * a[i - 1] + B[i])
        i = i + 1

    x[sizeM] = (F[sizeM] - A[sizeM] * b[sizeM - 1]) / (B[sizeM] + A[sizeM] * a[sizeM - 1])
    i = size - 2


    while (i > -1):
        x[i] = a[i] * x[i + 1] + b[i]
        i = i - 1
    return x 

def main(l, T, h_t, h_x, b0, b1, b2, f0, f1):
    
    max = int(2 * T / h_t)
    n = int(l / h_x) + 1
    m = int(T / h_t)
    A = [0] * n
    B = [0] * n
    C = [0] * n
    f_ = [0] * n
    w= [0] * n
    b = [0] * n
    f = [0] * n
    x = [0] * n
    j = 0


    while (j < m):
        i = 0
        while (i < n):
            if (j == 0):
                x[i] = i * h_x
                f[i] = 1 / l + f0 * math.cos(math.pi * x[i] / l) + f1 * math.cos(2 * math.pi * x[i] / l)
                f_[i] = f[i]
                b[i] = b0 + b1 * math.cos(math.pi * x[i] / l) + b2 * math.cos(2 * math.pi * x[i] / l)
            else:
                f_[i] = w[i]
            B[i] = 1 + 2 * h_t / (h_x * h_x) - h_t * b[i] 
            C[i] = -h_t / (h_x * h_x)
            A[i] = -h_t / (h_x * h_x)
            i = i + 1
        A[0] = 0
        B[0] = 1 + h_t / (h_x * h_x) - h_t * b[0]
        C[0] = -h_t / (h_x * h_x)
        A[n - 1] = -h_t / (h_x * h_x)
        B[n - 1] = 1 + h_t / (h_x * h_x) - h_t * b[n - 1]
        C[n - 1] = 0
        w = method(A, B, C, f_)
        j = j + 1
    w_I = w[0] + w[n-1]
    j = 1


    while(j < n - 1):
        if (j%2 == 1):
            w_I = w_I + 4 * w[j]
        else:
            w_I = w_I + 2 * w[j]
        j = j + 1
    w_I = w_I * h_x / 3
    for i in range(n):
        w[i] = w[i] / w_I
    j = 0
    y = [0] * n
    I = 0


    while (j < m):
        i = 0
        while (i < n):
            if (j == 0):
                f[i] = 1 / l + f0 * math.cos(math.pi * x[i] / l) + f1 * math.cos(2 * math.pi * x[i] / l)
                f_[i] = f[i]
                b[i] = b0 + b1 * math.cos(math.pi * x[i] / l) + b2 * math.cos(2 * math.pi * x[i] / l)
            else:
                    f_[i] = y[i]
            B[i] = 1 + 2 * h_t / (h_x * h_x) - h_t * b[i] + h_t * I
            C[i] = -h_t / (h_x * h_x)
            A[i] = -h_t / (h_x * h_x)
            i = i + 1
        A[0] = 0
        B[0] = 1 + h_t / (h_x * h_x) - h_t * b[0] + h_t* I
        C[0] = -h_t / (h_x * h_x)
        A[n - 1] = -h_t / (h_x * h_x)
        B[n - 1] = 1 + h_t / (h_x * h_x) - h_t * b[n - 1] + h_t * I
        C[n - 1] = 0
        y = method(A, B, C, f_)
        I = y[0] * b[0]+ y[n - 1] * b[n - 1]
        k = 1
        while (k < n - 1):
            if (k%2 == 1):
                I = I + 4 * y[k] * b[k]
            else:
                I = I + 2 * y[k] * b[k]
            k = k + 1
        I = I * h_x / 3
        j = j + 1


    global dop, _x, a, canvas
    dop = w
    _x = x
    fig = Figure(figsize=(8,5))
    a = fig.add_subplot(111)
    a.plot(x, f, label = "Start temp", color='blue')
    a.plot(x, y, label = "Fin temp", color='red')
    a.set_ylabel("t", fontsize=10)
    a.set_xlabel("x", fontsize=10)
    a.legend()
    root = Tk()
    root.title("Graphic")
    root.geometry("900x700")
    
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.get_tk_widget().place(relx=0.1, rely=0.1) #сдвиг по окну
    canvas.draw()
    btn = Button(root, text= "Построить", font = "Arial 10", command = continue_)
    btn.grid(row=0,column=0)


def continue_():
    a.plot(_x, dop, label = "Final temp A", color='green')
    a.legend()
    canvas.draw()