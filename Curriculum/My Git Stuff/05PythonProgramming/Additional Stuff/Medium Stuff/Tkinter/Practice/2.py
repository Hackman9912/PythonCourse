"""
2. Latin Translator
    Look at the following list of Latin words and their meanings.
        Latin       English
        sinister    left
        dexter      right
        medium      center
    Write a GUI program that translates the Latin words to English. The window should have
    three buttons, one for each Latin word. When the user clicks a button, the program displays 
    the English translation in a label.
"""
import tkinter as tk

window = tk.Tk()
window.title('Latin to English')
window.geometry('250x150')

# Functions
def translating():
    eng1 = tk.Label(text = 'left')
    eng1.grid(column = 2, row = 1)

    eng2 = tk.Label(text = 'right')
    eng2.grid(column = 2, row = 2)

    eng3 = tk.Label(text = 'center')
    eng3.grid(column = 2, row = 3)

# Label
label1 = tk.Label(text = 'Latin Word')
label1.grid(column=0, row=0, padx = (20,0))

label2=tk.Label(text = 'Sinister')
label2.grid(column=0, row=1)

label3=tk.Label(text = 'Dexter')
label3.grid(column=0, row=2)

label4=tk.Label(text = 'Medium')
label4.grid(column=0, row=3)

label5=tk.Label(text = 'English')
label5.grid(column = 2, row = 0)

# Button
button1 = tk.Button(text = "Click to translate", command = translating)
button1.grid(column = 1, row = 4, pady = 10)


window.mainloop()