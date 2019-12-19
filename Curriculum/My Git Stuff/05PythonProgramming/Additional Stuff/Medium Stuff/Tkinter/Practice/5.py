"""
5. Property Tax
    A county collects property taxes on the assessment value of property, which is 60 percent
    of the property’s actual value. If an acre of land is valued at $10,000, its assessment value
    is $6,000. The property tax is then $0.64 for each $100 of the assessment value. The tax
    for the acre assessed at $6,000 will be $38.40. Write a GUI program that displays the
    assessment value and property tax when a user enters the actual value of a property.
"""
import tkinter as tk
window = tk.Tk()
window.title('Taxes')
window.geometry('350x150')

# Functions
def taxes():
    act_val = float(entry1.get())
    tax = tk.Label(text = f'Your property tax is ${((act_val*.6)/100)*.64:.2f}.')
    tax.grid(column = 0, row = 1)

# Labels
label1 = tk.Label(text = 'Enter the actual value of your property:')
label1.grid(column = 0, row = 0)

# Entry
entry1 = tk.Entry()
entry1.grid(column = 1, row = 0)

# Button
button1 = tk.Button(text = 'Calculate!', command = taxes)
button1.grid(column = 0, row = 2)

window.mainloop()