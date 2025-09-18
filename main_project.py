from tkinter import *
from tkinter import messagebox
window=Tk()
window.configure(bg="red")
window.geometry("650x400")
label=Label(window,text="welcome to the denomination counter center")
label.pack()
def msg():
    msg_box=messagebox.showinfo("Information","Do you want to calculate notes")
    if msg_box=="ok":
        topwin()
btn=Button(window,text="Proceed",command=msg)
btn.pack()
def topwin():
    top=Toplevel()
    top.geometry("600x450")
    top.configure(bg="darkgrey")
    label=Label(top,text="Enter your amount")
    entry_box=Entry(top)
    label2=Label(top,text="Here is your denomination")
    l1=Label(top,text="$100")
    l2=Label(top,text="$50")
    l3=Label(top,text="$20")
    e1=Entry(top)
    e2=Entry(top)
    e3=Entry(top)
    def calculate():
        global amount
        amount=int(entry_box.get())
        note100=amount//100
        amount=amount%100
        note50=amount//50
        amount=amount%50
        note20=amount//20
        amount=amount%20
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e1.insert(END,str(note100))
        e2.insert(END,str(note50))
        e3.insert(END,str(note20))
    btn2=Button(top,text="Enter",command=calculate)
    label.place(x=230,y=50)
    entry_box.place(x=280,y=80)
    btn2.place(x=240,y=120)
    label2.place(x=140,y=170)
    l1.place(x=180,y=200)
    l2.place(x=180,y=230)
    l3.place(x=180,y=260)
    e1.place(x=270,y=200)
    e2.place(x=270,y=230)
    e3.place(x=270,y=260)
    top.mainloop()
window.mainloop()