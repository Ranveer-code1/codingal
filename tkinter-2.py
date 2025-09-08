from tkinter import *
window=Tk()
window.title("DEMO")
window.geometry("400x400")
for i in range(3):
    for j in range(3):
        frame=Frame(master=window,relief=RAISED,borderwidth=1)
        frame.grid(row=i,column=j,padx=5,pady=5)
        label=Label(frame,text=f"row={i} \n column={j}\n")
        label.pack()
window.mainloop()