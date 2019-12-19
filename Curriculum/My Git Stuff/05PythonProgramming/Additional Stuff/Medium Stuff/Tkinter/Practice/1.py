"""
1. Name and Address
    Write a GUI program that displays your name and address when a button is clicked. 
    When the user clicks the Show Info button, the program should display your name and
    address. Mess with the display to make it look neat.
"""
import tkinter as tk

window = tk.Tk()
window.title('PII')
window.geometry('400x400')
window.configure(bg = 'gray14')
# Functions
def display_data():
    name = str(entry1.get())
    address = str(entry2.get(1.0,'end-1c'))
    name_display = tk.Text(master=window, height=3, width=15)
    name_display.grid(column = 1, row = 3)
    name_display.insert(tk.END, name)
    name_display.configure(state='disabled', bg = 'black', fg = 'white')

    address_display = tk.Text(master=window, height=5, width=15)
    address_display.grid(column = 1, row = 4)
    address_display.insert(tk.END, address)
    address_display.configure(state='disabled', bg = 'black', fg = 'white')

# Label
label1 = tk.Label(text='Enter your name:')
label1.grid(column=0, row=0)
label1.configure(bg = 'black', fg = 'white')

label2=tk.Label(text = 'Enter your address:')
label2.grid(column=0, row=1)
label2.configure(bg = 'black', fg = 'white')
# Entry
entry1 = tk.Entry()
entry1.grid(column=2, row=0)
entry1.configure(bg = 'black', fg = 'white')

entry2 = tk.Text(master=window, height = 10, width = 15)
# entry2 = tk.Entry()
entry2.grid(column=2, row=1)
entry2.configure(bg = 'black', fg = 'white')

button1 = tk.Button(text='Click to display data:', command=display_data)
button1.grid(column=1, row=2)
button1.configure(bg = 'black', fg = 'white')

window.mainloop()