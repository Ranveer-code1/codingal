from tkinter import *
import random

window = Tk()
window.title("Rock, Paper, Scissors")
window.geometry("400x400")

label = Label(text="Enter your gesture (Rock, Paper, or Scissors):")
label.pack()

entry = Entry()
entry.pack()

result_label = Label(text="")
result_label.pack()

def fun():
    a = entry.get().capitalize() 
    s = random.choice(["Rock", "Paper", "Scissors"])  

    if (a == "Rock" and s == "Paper") or (a == "Scissors" and s == "Rock") or (a == "Paper" and s == "Scissors"):
       entry.insert(0, "Computer wins!")
    elif (a == "Rock" and s == "Scissors") or (a == "Paper" and s == "Rock") or (a == "Scissors" and s == "Paper"):
       entry.insert(0, "You win!")
    else:
        entry.insert(0, "It's a draw!")

btn = Button(text="Enter", command=fun)
btn.pack()

window.mainloop()
