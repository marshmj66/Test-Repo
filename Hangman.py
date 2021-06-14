import random
from tkinter import *
from tkinter.ttk import *

def add_body_parts():
    global count
    global appear
    appear += 1 
    #make the body appear

    if appear == 1:
        hangman.create_line(5, 5, 200, 200)
        count += 1
    if appear == 2:
        hangman.create_oval(50,-100,50,50)
        count += 1
    if appear == 3:
        hangman.create_line(-200, 200, 200, 200, fill='blue',width=5)
        count += 1
    if appear == 4:
        hangman.create_line(5, 5, 200, 200, fill='black', width=5)
        count += 1
    if appear == 5:
        hangman.create_line(5, 5, 200, 200, fill='yellow', width=5)
        count += 1
    if appear == 6:
        hangman.create_line(5, 5, 200, 200, fill='red', width=5)
        count += 1
    if count >= 6:
        hangman2.config(text="game over your out of tries")
        hangman.destroy()
    print(count)

window = Tk()
#window setup (images and etc)
window.geometry('500x500')
window.title('Hangman')
icon = PhotoImage(file = "C:\\Users\\Marshall Johnson\\Downloads\\2021_01_25_confused-dream-desc-16498478.png")
window.iconphoto(True, icon)
window.config(background= "light yellow")

# features (Buttons and etc)
body = [[''],
        ['','',''],
        ['','']]
body2 = []
count = 0
appear = 0

hangman = Canvas(window, height=400, width=400)

hangman.pack()

hangman2 = Label(window, width = 400)
hangman2.pack()


button = Button(window,text='press me',command=add_body_parts)
button.pack()


window.mainloop()