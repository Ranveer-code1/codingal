from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("Unidentified source")
def virus():
    messagebox.showwarning("Warning","Virus detected")
btn=Button(text="Enter",command=virus)
btn.pack()
window.mainloop()