"""
3. Miles Per Gallon Calculator
    Write a GUI program that calculates a car’s gas mileage. The program’s window should
    have Entry widgets that let the user enter the number of gallons of gas the car holds, and
    the number of miles it can be driven on a full tank. When a Calculate MPG button is
    clicked, the program should display the number of miles that the car may be driven per gallon of 
    gas. Use the following formula to calculate miles-per-gallon:

        MPG = miles/gallons
"""
import tkinter as tk 

window = tk.Tk()
window.title('MPG')
window.geometry('600x200')

# Functions
def mpg():
    gal = int(entry1.get())
    miles = int(entry2.get())
    tot = tk.Label(text = f'Your MPG is {miles/gal:.2f}.')
    tot.grid(column = 1, row = 3)

# Label
label1 = tk.Label(text = 'Enter the gallons of gas your car holds:')
label1.grid(column = 0, row = 0)

label2 = tk.Label(text = "Enter how many miles your car can travel on a tank:")
label2.grid(column = 0, row = 1)

# Entry
entry1 = tk.Entry()
entry1.grid(column = 2, row = 0)

entry2 = tk.Entry()
entry2.grid(column = 2, row = 1)

button1 = tk.Button(text = 'Calculate!', command = mpg)
button1.grid(column = 1, row = 2)

window.mainloop()
