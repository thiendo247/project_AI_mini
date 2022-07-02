
from tkinter import*
from tkinter.ttk import*
from time import strftime
root = Tk()
root.title("Dong ho ky thua so by Thiendoo")
def clock():
    string  = strftime('%H:%M:%S:%p')
    label.config(text=string)
    label.after(1000, clock)


label = Label(root, font=("Digital-7",100), background="black", foreground="blue")
label.pack(anchor="center")
clock()
root.mainloop()

