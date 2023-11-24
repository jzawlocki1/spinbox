from tkinter import *

root =Tk()

root.geometry("500x500")
fst=5
var = DoubleVar(value=2)
def fstart():
    print(myspin.get())
    fst = int(myspin.get())
    print("ft: ", fst)
    print("ft: ", var)
lbl1 = Label(root, text="Freq Start")
lbl1.place(x=4, y=4)
myspin1 = Spinbox(root, width=8, from_=1, to=10,textvariable=var, command=fstart)
myspin1.place(x=60, y=4)

lbl2 = Label(root, text="Freq Start")
lbl2.place(x=4, y=30)
myspin2 = Spinbox(root, width=8, from_=1, to=10,textvariable=var, command=fstart)
myspin2.place(x=60, y=30)


var.set(5)
root.mainloop()
