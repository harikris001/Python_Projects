from tkinter import *

calc = Tk()
calc.title("Simple Calculator")
numbers = Entry(calc,fg='grey')
button_1 = Button(calc,text="1")
button_2 = Button(calc,text="2")
button_3 = Button(calc,text="3")
button_4 = Button(calc,text="4")
button_5 = Button(calc,text="5")
button_6 = Button(calc,text="6")
button_7 = Button(calc,text="7")
button_8 = Button(calc,text="8")
button_9 = Button(calc,text="9")
button_0 = Button(calc,text="0")
button_plus = Button(calc,text="+",command = lambda add(numbers.get())
button_equal = Button(calc,text='=')
button_clear = Button(calc,text='CE')

def add(num):
  firstnum = int(numbers.get())
  global fnum = num
  secondnum = int(numbers.get())
  global result = firstnum + secondnum

numbers.grid(row=0,column=0,columnspan=4)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_6.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_4.grid(row=2,column=2)
button_3.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_1.grid(row=3,column=2)
button_0.grid(row=4,column=0)
button_equal.grid(row=4,column=1)
button_clear.grid(row=4,column=2)


calc.mainloop()
