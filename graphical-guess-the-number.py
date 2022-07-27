import random
import tkinter as tk
from tkinter import * 
root = Tk()
root.title("Guess the Number Game")
random_number = random.randint(1,100)
user_number = 0
#root.configure(bg="yellow")
#root.iconphoto(False, tk.PhotoImage(file='images/7111.png'))
e = Entry(root, width=35, borderwidth=5, bg="white", fg="blue")
e.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
tatti = 9

def button_guess():
    current = e.get()
    global user_number 
    user_number = current
    e.delete(0, END)
    my_label4 = Label(root, text="", command=number_guess())


def number_guess():
    global user_number
    global tatti
    if int(user_number) == random_number:
        my_label4 = Label(root, text="You guess the correct number")
        my_label4.grid(row=5, column=1)
        tatti = tatti -1
        

        
    elif int(user_number) > random_number:
        my_label4 = Label(root, text="Decrease ur number")
        my_label4.grid(row=5, column=1)
        tatti = tatti - 1 
    elif int(user_number) < random_number:
        my_label4 = Label(root, text="Increase ur number")
        my_label4.grid(row=5, column=1)
        tatti = tatti - 1 
    

            
my_label3 =Button(root, text="Guess number", bg="white",fg="red", command=button_guess)
my_label2 =Label(root, text="Guess a number from 1 to 100")

my_label2.grid(row=1, column=1)
my_label3.grid(row=3, column=1)
    



root.mainloop()
    

