
from math import sin, cos, tan, sqrt, log
import tkinter as tk
from math import *
root = tk.Tk()
root.title("Scientific Calculator")
expression = ""
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)
def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""
def clear():
    global expression
    expression = ""
    equation.set("")
equation = tk.StringVar()
expression_field = tk.Entry(root, textvariable=equation)
expression_field.grid(columnspan=4, ipadx=70)
button1 = tk.Button(root, text=' 1 ', command=lambda: press(1), height=1, width=7)
button1.grid(row=2, column=0)

button2 = tk.Button(root, text=' 2 ', command=lambda: press(2), height=1, width=7)
button2.grid(row=2, column=1)

button3 = tk.Button(root, text=' 3 ', command=lambda: press(3), height=1, width=7)
button3.grid(row=2, column=2)

button4 = tk.Button(root, text=' 4 ', command=lambda: press(4), height=1, width=7)
button4.grid(row=3, column=0)
button5 = tk.Button(root, text=' 5 ', command=lambda: press(5), height=1, width=7)
button5.grid(row=3, column=1)

button6 = tk.Button(root, text=' 6 ', command=lambda: press(6), height=1, width=7)
button6.grid(row=3, column=2)

button7 = tk.Button(root, text=' 7 ', command=lambda: press(7), height=1, width=7)
button7.grid(row=4, column=0)

button8 = tk.Button(root, text=' 8 ', command=lambda: press(8), height=1, width=7)
button8.grid(row=4, column=1)

button9 = tk.Button(root, text=' 9 ', command=lambda: press(9), height=1, width=7)
button9.grid(row=4, column=2)

button0 = tk.Button(root, text=' 0 ', command=lambda: press(0), height=1, width=7)
button0.grid(row=5, column=0)


buttonAdd = tk.Button(root, text=' + ', command=lambda: press('+'), height=1, width=7)
buttonAdd.grid(row=2, column=3)

buttonSubtract = tk.Button(root, text=' - ', command=lambda: press('-'), height=1, width=7)
buttonSubtract.grid(row=3, column=3)

buttonMultiply = tk.Button(root, text=' * ', command=lambda: press('*'), height=1, width=7)
buttonMultiply.grid(row=4, column=3)

buttonDivide = tk.Button(root, text=' / ', command=lambda: press('/'), height=1, width=7)
buttonDivide.grid(row=5, column=3)
buttonSin = tk.Button(root, text='sin', command=lambda: press('sin('), height=1, width=7)
buttonSin.grid(row=6, column=0)

buttonCos = tk.Button(root, text='cos', command=lambda: press('cos('), height=1, width=7)
buttonCos.grid(row=6, column=1)

buttonTan = tk.Button(root, text='tan', command=lambda: press('tan('), height=1, width=7)
buttonTan.grid(row=6, column=2)

buttonSqrt = tk.Button(root, text='√', command=lambda: press('sqrt('), height=1, width=7)
buttonSqrt.grid(row=7, column=0)

buttonLog = tk.Button(root, text='log', command=lambda: press('log('), height=1, width=7)
buttonLog.grid(row=7, column=1)
buttonDecimal = tk.Button(root, text='.', command=lambda: press('.'), height=1, width=7)
buttonDecimal.grid(row=5, column=2)

buttonOpenParen = tk.Button(root, text='(', command=lambda: press('('), height=1, width=7)
buttonOpenParen.grid(row=7, column=2)

buttonCloseParen = tk.Button(root, text=')', command=lambda: press(')'), height=1, width=7)
buttonCloseParen.grid(row=7, column=3)

buttonPower = tk.Button(root, text='^', command=lambda: press('**'), height=1, width=7)
buttonPower.grid(row=8, column=0)

buttonMod = tk.Button(root, text='mod', command=lambda: press('%'), height=1, width=7)
buttonMod.grid(row=8, column=1)

buttonExp = tk.Button(root, text='exp', command=lambda: press('exp('), height=1, width=7)
buttonExp.grid(row=8, column=2)

equal = tk.Button(root, text=' = ', command=equalpress, height=1, width=7)
equal.grid(row=6, column=3)
clear = tk.Button(root, text='Clear', command=clear, height=1, width=7)
clear.grid(row=5, column='1')
root.mainloop()
