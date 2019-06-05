from tkinter import *

window = Tk()
def km_to_miles():
    print(e1_value.get())
    miles = float(e1_value.get())
    t1.insert(END,miles*1000)
    t2.insert(END,miles* 2.20462)
    t3.insert(END,miles*35.274)

w = Label(window,text="Kg")
w.grid(row=0,column=0)
b1 = Button(window,text="convert",command=km_to_miles)
b1.grid(row=0,column=2)

e1_value = StringVar()

e1 = Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1 = Text(window,height=1,width=20)
t1.grid(row=1,column=0)
t2 = Text(window,height=1,width=20)
t2.grid(row=1,column=1)
t3 = Text(window,height=1,width=20)
t3.grid(row=1,column=2)
window.mainloop()
