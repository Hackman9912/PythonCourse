"""
6. Joe’s Automotive
    Joe’s Automotive performs the following routine maintenance services:
        • Oil change          —   $26.00
        • Lube job            —   $18.00
        • Radiator flush      —   $30.00
        • Transmission flush  —   $80.00
        • Inspection          —   $15.00
        • Muffler replacement —   $100.00
        • Tire rotation       —   $20.00
    Write a GUI program with check buttons that allow the user to select any or all of these
    services. When the user clicks a button the total charges should be displayed.
"""
import tkinter as tk 
window = tk.Tk()
window.title('Auto Shop')
window.geometry('460x400')

# Functions
def checkout():
    total = checked3.get() + checked4.get() + checked5.get() + checked6.get() + checked7.get() + checked8.get() + checked9.get()
    print(f'Here is your total ${total:.2f}')
    label10 = tk.Label(wraplength = 60, text = f'Here is your total ${total:.2f}')
    label10.grid(column = 3, row = 10)


# Labels
label1 = tk.Label(text = 'Joes Automotive')
label1.grid(column = 0, row = 0)

label2 = tk.Label(text = 'Joe’s Automotive performs the following routine maintenance services:')
label2.grid(column = 0)

label3 = tk.Label(text = '• Oil change---------------------------------$26.00')
label3.grid(column = 0, row = 2, padx = (0,100))
checked3 = tk.IntVar()
button3 = tk.Checkbutton(variable = checked3, onvalue = 26, offvalue = 0, command = checkout)
button3.grid(column = 3, row = 2, padx = (20,0))

label4 = tk.Label(text = '• Lube job-----------------------------------$18.00')
label4.grid(column = 0, row = 3, padx = (0,100))
checked4 = tk.IntVar()
button4 = tk.Checkbutton(variable = checked4, onvalue = 18, offvalue = 0, command = checkout)
button4.grid(column = 3, row = 3, padx = (20,0))

label5 = tk.Label(text = '• Radiator flush-------------------------------$30.00')
label5.grid(column = 0, row = 4, padx = (0,100))
checked5 = tk.IntVar()
button5 = tk.Checkbutton(variable = checked5, onvalue = 30, offvalue = 0, command = checkout)
button5.grid(column = 3, row = 4, padx = (20,0))

label6 = tk.Label(text = '• Transmission flush--------------------------$80.00')
label6.grid(column = 0, row = 5, padx = (0,100))
checked6 = tk.IntVar()
button6 = tk.Checkbutton(variable = checked6, onvalue = 80, offvalue = 0, command = checkout)
button6.grid(column = 3, row = 5, padx = (20,0))

label7 = tk.Label(text = '• Inspection----------------------------------$15.00')
label7.grid(column = 0, row = 6, padx = (0,100))
checked7 = tk.IntVar()
button7 = tk.Checkbutton(variable = checked7, onvalue = 15, offvalue = 0, command = checkout)
button7.grid(column = 3, row = 6, padx = (20,0))

label8 = tk.Label(text = '• Muffler replacement-------------------------$100.00')
label8.grid(column = 0, row = 7, padx = (0,100))
checked8 = tk.IntVar()
button8 = tk.Checkbutton(variable = checked8, onvalue = 100, offvalue = 0, command = checkout)
button8.grid(column = 3, row = 7, padx = (20,0))

label9 = tk.Label(text = '• Tire rotation-----------------------------------$20.00')
label9.grid(column = 0, row = 8, padx = (0,100))
checked9 = tk.IntVar()
button9 = tk.Checkbutton(variable = checked9, onvalue = 20, offvalue = 0, command = checkout)
button9.grid(column = 3, row = 8, padx = (20,0))



# Button
button1 = tk.Button(text = 'Check Out', command = lambda: exit())
button1.grid(column = 3, row = 9)
window.mainloop()





























