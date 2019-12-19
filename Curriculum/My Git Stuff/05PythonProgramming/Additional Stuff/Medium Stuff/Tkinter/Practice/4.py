"""
4. Celsius to Fahrenheit
    Write a GUI program that converts Celsius temperatures to Fahrenheit temperatures. The user
    should be able to enter a Celsius temperature, click a button, and then see the equivalent
    Fahrenheit temperature. Use the following formula to make the conversion:

        F = (9/5)C + 32

    F is the Fahrenheit temperature and C is the Celsius temperature.
"""
import tkinter as tk 
window = tk.Tk()
window.title('C to F')
window.geometry('300x150')

# Functions
def conv():
    cels = float(entry1.get())
    fahr = tk.Label(text = f'{cels:.2f} Celsius is {(9/5)*cels+32:.2f} Fahrenheit.')
    fahr.grid(column = 0, row = 1)

# Labels
label1 = tk.Label(text = 'Enter the degrees C to convert to F:')
label1.grid(column = 0, row = 0)

# Entry
entry1 = tk.Entry()
entry1.grid(column = 1, row = 0)

# Button
button1 = tk.Button(text = 'Calculate!', command = conv)
button1.grid(column = 0, row = 2)

window.mainloop()