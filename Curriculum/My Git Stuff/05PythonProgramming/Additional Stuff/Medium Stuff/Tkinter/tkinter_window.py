# Access tkinter
import tkinter as tk

# instantiate tkinter object
window = tk.Tk()

# set the title for your window
window.title('First tkinter app')

# Set the size of your window
window.geometry('400x400')

# Adding a label: text = 'What your label says', font = "your font name", the size as a number
title = tk.Label(text = 'Hello world!', font = ('Times New Roman', 24))

# grid() tells you where you want the label, (0,0) is default
title.grid(column = 0, row = 0)


# title.pack() just kind of shoves stuff into the frame. Grid is better
# title.pack()

# padx and pady will increase space between things on an x and y axis. takes 2 arguments for in front and behind  padx = (10,10), pady = (10,10)
# Adding a Button
button1 = tk.Button(text = 'Click me', bg = 'red')
button1.grid(column = 0, row = 1)


# Adding an Entry
entry_field1 = tk.Entry()
entry_field1.grid(column=0, row=2)

# Text field
text_field = tk.Text(master=window, height = 10, width = 30)
text_field.grid(column = 0, row = 3)


# Opens and keeps tkinter window open. It is like calling your 'function'
# Everything you do must be between this and instantiating your window
# This is always at the bottom.
# It continuously puts the window in a loop to keep it open
window.mainloop()