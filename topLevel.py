from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("Unidentified source")
window.geometry("500x500")
window.configure(bg="black")
def virus():
   top=Toplevel()
   top.title("TOP")
   top.geometry("250x250")
   top.configure(bg="red")
btn=Button(text="Enter",command=virus)
btn.pack()
window.mainloop()