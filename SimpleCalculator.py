# Import the tkinter GUI module for Python
from tkinter import *

    
#The Display of the programs
calc = Tk() #simplify the Tk module function
calc.title("Calculator") #Set the title or name of window
output = "" 
varStr = StringVar()

text_Display = Entry(calc, font = ('comic sans', 20, 'bold'), textvariable = varStr,
                     bd=20, insertwidth = 4,bg = 'spring green', justify = 'right').grid(columnspan=4)


#The Button Functions and Definitions
def clickButton(numbers):
    global output
    output=output + str(numbers)
    varStr.set(output)

def clearButton():
    global output
    output=""
    varStr.set("")

def equalButton():
    global output
    total=str(eval(output))
    varStr.set(total)
    output=""

#Make the first row of buttons
b7 = Button(calc, padx = 10, bd = 8, fg = "black", bg = 'PaleGreen1', font=('comic sans', 20, 'bold'),
            text="7", command=lambda:clickButton(7)).grid(row=1, column=0)

b8 = Button(calc, padx = 10, bd = 8, fg = "black", bg = 'PaleGreen1', font=('comic sans', 20, 'bold'),
            text="8", command=lambda:clickButton(8)).grid(row=1, column=1)

b9 = Button(calc, padx = 10, bd = 8, fg = "black", bg = 'PaleGreen1', font=('comic sans', 20, 'bold'),
            text="9", command=lambda:clickButton(9)).grid(row=1, column=2)

bdiv = Button(calc, padx = 10, bd = 8, fg = "black", bg = 'PaleGreen1', font=('comic sans', 20, 'bold'),
            text="÷", command=lambda:clickButton('/')).grid(row=1, column=3) #find out how to get the division sign instead of the backslash sign

b4 = Button(calc, padx = 10, bd = 8, fg = "black", bg = 'PaleGreen1', font=('comic sans', 20, 'bold'),
            text="4", command=lambda:clickButton(4)).grid(row=2, column=0)

b5 = Button(calc, padx = 10, bd = 8, fg = "black", bg = 'PaleGreen1', font=('comic sans', 20, 'bold'),
            text="5", command=lambda:clickButton(5)).grid(row=2, column=1)

b6 = Button(calc, padx = 10, bd = 8, fg = "black", bg = 'PaleGreen1', font=('comic sans', 20, 'bold'),
            text="6", command=lambda:clickButton(6)).grid(row=2, column=2)

bmult = Button(calc, padx = 12, bd = 8, fg = "black", bg = 'PaleGreen1', font=('comic sans', 20, 'bold'),
            text="*", command=lambda:clickButton('*')).grid(row=2, column=3)

b1 = Button(calc, padx = 10, bd = 8, fg = "black", bg = 'PaleGreen1', font=('comic sans', 20, 'bold'),
            text="1", command=lambda:clickButton(1)).grid(row=3, column=0)

b2 = Button(calc, padx = 10, bd = 8, fg = "black", bg = 'PaleGreen1', font=('comic sans', 20, 'bold'),
            text="2", command=lambda:clickButton(2)).grid(row=3, column=1)

b3 = Button(calc, padx = 10, bd = 8, fg = "black", bg = 'PaleGreen1', font=('comic sans', 20, 'bold'),
            text="3", command=lambda:clickButton(3)).grid(row=3, column=2)

bminus = Button(calc, padx = 14, bd = 8, fg = "black", bg = 'PaleGreen1', font=('comic sans', 20, 'bold'),
            text="-", command=lambda:clickButton('-')).grid(row=3, column=3)

b0 = Button(calc, padx = 10, bd = 8, fg = "black", bg = 'PaleGreen1', font=('comic sans', 20, 'bold'),
            text="0", command=lambda:clickButton(0)).grid(row=4, column=0)

bequal = Button(calc, padx = 9, bd = 8, fg = "black", bg = 'PaleGreen4', font=('comic sans', 20, 'bold'),
            text="=", command=equalButton).grid(row=4, column=2)

bplus = Button(calc, padx = 10, bd = 8, fg = "black", bg = 'PaleGreen1', font=('comic sans', 20, 'bold'),
            text="+", command=lambda:clickButton('+')).grid(row=4, column=3)

bclear = Button(calc, padx = 10, pady = 8, bd = 8, fg ="black", bg = 'PaleGreen1', font=('comic sans', 15, 'bold'),
                text="CE", command=lambda:clearButton()).grid(row=4, column=1)




calc.mainloop()
