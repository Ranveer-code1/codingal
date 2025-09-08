from tkinter import *
window=Tk()
window.title("DEMO")
window.geometry("400x400")

label=Label(text="Enter your name")
label.pack()
box=Entry()
box.pack()
box2=Entry()
box2.pack()

def fun():
    a=box.get()
    box2.delete(0,END)
    box2.insert(0,a)
btn=Button(text="Submit",command=fun)
btn.pack()
window.mainloop()