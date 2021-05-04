import tkinter as tk
from tkinter import *
import math
from tkinter import messagebox


win = Tk()
win.geometry("300x500")
win.resizable(0, 0)
win.title("Samuel's Triangle Calculator")
win.configure(bg="Grey")

canvas = Canvas(win, width=296, height=210, bg="Black")
canvas.place(x=0, y=0)

atextvar = StringVar()
btextvar = StringVar()
ctextvar = StringVar()
aatextvar = StringVar()
abtextvar = StringVar()


def reset():
    atextvar.set("")
    btextvar.set("")
    ctextvar.set("")
    aatextvar.set("")
    abtextvar.set("")

    canvas = Canvas(win, width=296, height=210, bg="Black")
    canvas.place(x=0, y=0)
    canvas.create_line(90, 60, 90, 170, 210, 170, 90, 60, fill='White', width=2)
    canvas.create_line(90, 155, 105, 155, 105, 170, fill='White', width=2)

    aside = Label(win, text="a", bg="Black", fg="White")
    aside.place(x=75, y=110)
    bside = Label(win, text="b", bg="Black", fg="White")
    bside.place(x=140, y=174)
    cside = Label(win, text="c", bg="Black", fg="White")
    cside.place(x=150, y=93)
    angleb = Label(win, text="B", bg="Black", fg="White")
    angleb.place(x=75, y=45)
    anglea = Label(win, text="A", bg="Black", fg="White")
    anglea.place(x=215, y=165)

def draw(h, v):

    if h > v:
        hd = 150
        dif = h - v
        per = dif / h
        vd = hd - (hd * per)

        vpoint = 105
        hpoint = 148

        yup = vpoint - (vd / 2)
        ydown = yup + vd

        xleft = hpoint - (hd / 2)
        xright = xleft + hd

        canvas = Canvas(win, width=296, height=210, bg="Black")
        canvas.place(x=0, y=0)
        canvas.create_line(xleft, yup, xleft, ydown, xright, ydown, xleft, yup, fill='White', width=2)

        aside = Label(win, text="a", bg="Black", fg="White")
        aside.place(x=xleft - 20, y=vpoint - 10)
        bside = Label(win, text="b", bg="Black", fg="White")
        bside.place(x=hpoint - 10, y=ydown + 5)
        cside = Label(win, text="c", bg="Black", fg="White")
        cside.place(x=hpoint - 5, y=vpoint - 25)
        angleb = Label(win, text="B", bg="Black", fg="White")
        angleb.place(x=(hpoint - 5) - (hd / 2), y=(vpoint - 25) - (vd / 2))
        anglea = Label(win, text="A", bg="Black", fg="White")
        anglea.place(x=(hpoint + 5) + (hd / 2), y=(vpoint - 10) + (vd / 2))

    if h < v:
        vd = 150
        dif = v - h
        per = dif / v
        hd = vd - (vd * per)

        vpoint = 105
        hpoint = 148

        yup = vpoint - (vd / 2)
        ydown = yup + vd

        xleft = hpoint - (hd / 2)
        xright = xleft + hd

        canvas = Canvas(win, width=296, height=210, bg="Black")
        canvas.place(x=0, y=0)
        canvas.create_line(xleft, yup, xleft, ydown, xright, ydown, xleft, yup, fill='White', width=2)

        aside = Label(win, text="a", bg="Black", fg="White")
        aside.place(x=xleft - 20, y=vpoint - 10)
        bside = Label(win, text="b", bg="Black", fg="White")
        bside.place(x=hpoint, y=ydown + 5)
        cside = Label(win, text="c", bg="Black", fg="White")
        cside.place(x=hpoint, y=vpoint - 25)
        angleb = Label(win, text="B", bg="Black", fg="White")
        angleb.place(x=(hpoint - 5) - (hd / 2), y=(vpoint - 25) - (vd / 2))
        anglea = Label(win, text="A", bg="Black", fg="White")
        anglea.place(x=(hpoint + 5) + (hd / 2), y=(vpoint - 10) + (vd / 2))

def calculate():

    try:
        # --- a ---
        if atextvar.get() != "":
            # --- b ---
            if btextvar.get() != "":
                convert1 = float(atextvar.get()) ** 2
                convert2 = float(btextvar.get()) ** 2
                convert3 = convert1 + convert2
                convert4 = math.sqrt(convert3)
                convert5 = float('%.2f' % (convert4))
                ctextvar.set(str(convert5))  # ------------------------------ found c
                a = float(atextvar.get())
                b = float(btextvar.get())
                convert6 = a / b
                A = math.degrees(math.atan(convert6))
                aatextvar.set(str(A))  # ------------------------------------ found A
                abtextvar.set(str(float('%.2f' % (90 - A))))  # ------------- found B
                convert6 = float('%.2f' % (b))
                btextvar.set(convert6)

            # --- c ---
            if ctextvar.get() != "":
                convert1 = float(atextvar.get()) ** 2
                convert2 = float(ctextvar.get()) ** 2
                convert3 = convert2 - convert1
                convert4 = math.sqrt(convert3)
                convert5 = float('%.2f' % (convert4))
                btextvar.set(str(convert5))  # ------------------------------ found b
                a = float(atextvar.get())
                b = float(ctextvar.get())
                convert6 = float(a / b)
                convert7 = math.degrees(math.acos(convert6))
                convert8 = float('%.2f' % (convert7))
                abtextvar.set(str(convert8))  # ----------------------------- found B
                aatextvar.set(float('%.2f' % (90 - convert8)))  # ----------- found A

                v = float(a)
                h = float(btextvar.get())
                draw(h, v)

            # --- A ---
            if aatextvar.get() != "":
                a = float(atextvar.get())
                A = float(aatextvar.get())
                convert1 = a / math.tan(math.radians(A))
                convert2 = float('%.2f' % (convert1))
                btextvar.set(str(convert2))  # ----------------------------- found b
                convert3 = a / math.sin(math.radians(A))
                convert4 = float('%.2f' % (convert3))
                ctextvar.set(str(convert4))  # ------------------------------ found c
                abtextvar.set(str(float('%.2f' % (90 - A))))  # ----------- found B
            # --- B ---
            if abtextvar.get() != "":
                a = float(atextvar.get())
                B = float(abtextvar.get())
                convert1 = float(a / math.cos(math.radians(B)))
                ctextvar.set(str(convert1))  # ------------------------------ found c
                convert2 = (convert1 ** 2) - a ** 2
                convert3 = math.sqrt(convert2)
                convert4 = float('%.2f' % (convert3))
                btextvar.set(str(convert4))  # ----------------------------- found b
                aatextvar.set(float('%.2f' % (90 - B)))  # ---------------- found A

        # --- b ---
        if btextvar.get() != "":

            # --- c ---
            if ctextvar.get() != "":
                convert1 = float(ctextvar.get()) ** 2
                convert2 = float(btextvar.get()) ** 2
                convert3 = convert1 - convert2
                convert4 = math.sqrt(convert3)
                convert5 = float('%.2f' % (convert4))
                atextvar.set(str(convert5))  # ---------------------- found a

                b = float(btextvar.get())
                c = float(ctextvar.get())
                convert6 = float(b / c)
                convert7 = math.degrees(math.acos(convert6))
                A = float('%.2f' % (convert7))
                aatextvar.set(str(A))  # -------------------- found A
                abtextvar.set(str(float('%.2f' % (90 - A))))  # ----------- found B
            # --- B ---
            if abtextvar.get() != "":
                b = float(btextvar.get())
                convert1 = float(abtextvar.get())
                B = float('%.2f' % (convert1))
                a = b / math.tan(math.radians(B))
                atextvar.set(str(a))  # ---------------------------------- found a
                convert2 = (a ** 2) + (b ** 2)
                convert3 = float('%.2f' % (convert2))
                convert4 = math.sqrt(convert3)
                ctextvar.set(str(convert4))  # --------------------------- found c
                aatextvar.set(float('%.2f' % (90 - B)))  # --------------- found A
            # --- A ---
            if aatextvar.get() != "":
                A = float(aatextvar.get())
                abtextvar.set(str(float('%.2f' % (90 - A))))  # ---------- found B
                b = float(btextvar.get())
                convert0 = b / math.cos(math.radians(A))
                c = float('%.2f' % (convert0))
                ctextvar.set(str(c))  # ---------------------------------- found c
                convert1 = (c ** 2) - (b ** 2)
                convert2 = math.sqrt(convert1)
                a = float('%.2f' % (convert2))
                atextvar.set(str(a))  # ---------------------------------- found a

        # --- c ---
        if ctextvar.get() != "":
            if aatextvar.get() != "":
                A = float(aatextvar.get())
                abtextvar.set(str(float('%.2f' % (90 - A))))  # --------- found B
                c = float(ctextvar.get())
                convert1 = math.cos(math.radians(A)) * c
                convert2 = float('%.2f' % (convert1))
                btextvar.set(str(convert2))  # -------------------------- found b
                b = convert1
                convert3 = (c ** 2) - (b ** 2)
                convert4 = math.sqrt(convert3)
                a = float('%.2f' % (convert4))
                atextvar.set(str(a))  # --------------------------------- found a

            if abtextvar.get != "":
                c = float(ctextvar.get())
                B = float(abtextvar.get())
                convert1 = math.cos(math.radians(B)) * c
                convert2 = float('%.2f' % (convert1))
                atextvar.set(str(convert2))  # ------------------------- found a
                convert3 = (c ** 2) - (convert2 ** 2)
                b = math.sqrt(convert3)
                btextvar.set(str(b))  # -------------------------------- found b
                aatextvar.set(float('%.2f' % (90 - B)))  # --------------- found A
    except:

        messagebox.showerror("Value Error!", "Wrong value input"), ValueError

    v = float(atextvar.get())
    h = float(btextvar.get())
    draw(h, v)

class Triangle(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

        canvas.create_line(90, 60, 90, 170, 210, 170, 90, 60, fill='White', width=2)
        canvas.create_line(90, 155, 105, 155, 105, 170, fill='White', width=2)

        aside = Label(win, text="a", bg="Black", fg="White")
        aside.place(x=75, y=110)
        bside = Label(win, text="b", bg="Black", fg="White")
        bside.place(x=140, y=174)
        cside = Label(win, text="c", bg="Black", fg="White")
        cside.place(x=150, y=93)
        angleb = Label(win, text="B", bg="Black", fg="White")
        angleb.place(x=75, y=45)
        anglea = Label(win, text="A", bg="Black", fg="White")
        anglea.place(x=215, y=165)

        calcbutton = Button(win, text="Calculate", width=15, command=calculate)
        calcbutton.place(x=30, y=230)
        resetbutton = Button(win, text="Reset", width=15, command=reset)
        resetbutton.place(x=155, y=230)

        atext = Label(win, text="a = ", bg="Grey", font=12)
        atext.place(x=40, y=290)
        btext = Label(win, text="b = ", bg="Grey", font=12)
        btext.place(x=40, y=320)
        ctext = Label(win, text="c = ", bg="Grey", font=12)
        ctext.place(x=40, y=350)
        aatext = Label(win, text="Angle A = ", bg="Grey", font=12)
        aatext.place(x=40, y=380)
        abtext = Label(win, text="Angle B = ", bg="Grey", font=12)
        abtext.place(x=40, y=410)

        aentry = Entry(win, textvariable=atextvar)
        aentry.place(x=130, y=290)
        bentry = Entry(win, textvariable=btextvar)
        bentry.place(x=130, y=320)
        centry = Entry(win, textvariable=ctextvar)
        centry.place(x=130, y=350)
        aaentry = Entry(win, textvariable=aatextvar)
        aaentry.place(x=130, y=380)
        abentry = Entry(win, textvariable=abtextvar)
        abentry.place(x=130, y=410)


Triangle()
win.mainloop()
