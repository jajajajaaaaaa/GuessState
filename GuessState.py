import tkinter
from tkinter import *
import random
from tkinter import messagebox
from random import shuffle 



answer = states = ['Washington', 'Oregon', 'California', 'Ohio', 'Nebraska', 'Colorado', 'Michigan', 'Massachusetts', 'Florida', 'Texas', 'Oklahoma', 'Hawaii', 'Alaska', 'Utah', 'Virginia', 'Minnesota', 'Illinois', 'Indiana', 'Kentucky', 'Tennessee', 'Georgia', 'Alabama', 'Mississippi', 'Maine', 'Vermont', 'Connecticut', 'Wyoming', 'Montana', 'Kansas', 'Iowa', 'Pennsylvania', 'Maryland', 'Missouri', 'Arizona', 'Nevada', 'Wisconsin', 'Delaware', 'Idaho', 'Arkansas', 'Louisiana']


words = []

for i in answer:
    word = list(i)
    shuffle(word)
    words.append(word)

num = random.randint(0,len(words))


def initial():
    global words, num
    lb1.configure(text = words[num])

def ans_check():
    global words, num, answer
    user_input = e1.get()
    if user_input == answer[num]:
        messagebox.showinfo("Success")
        reset()
    else:
        messagebox.showinfo("Error")
        e1.delete(0,END)

def Reset():
    global words,num,answer
    num = random.randint(0,len(words))
    lb1.configure(text = words[num])
    e1.delete(0,END)


root = Tk()
root.geometry("350x400+400+300")
root.title("Jumbbled")
root.configure(background = "#8076a3")


my_laber = Label(root, text = "", bg = "#dea6af", fg = "#282828",font = ("Georgia", 20))
my_laber.pack()

lb1 = Label(root, font = ("Georgia", 20), bg = "#7c677f", fg = "#ffaaab")
lb1.pack(pady = 40, ipady = 10, ipadx = 10)

answer12 = StringVar()
e1 = Entry(root, bg = "white", font = ("Georgia", 16), textvariable = answer)
e1.pack(ipady = 5, ipadx = 5)

#Gilaki
button1 = Button(root, text = "Check", width = 20, command = ans_check, bg = "#7c677f", fg = "#ffaaab", font = 'Georgia, 15')
button1.pack(pady = 40)

button2 = Button(root, text = "Reset", width = 20, command = Reset, bg = "#7c677f", fg = "#ffaaab", font = 'Georgia, 15')
button2.pack()


initial()

root.mainloop()

