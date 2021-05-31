import math
from tkinter import *

root = Tk()
root.title("Mario Calculator")

e = Entry(root,width=70,borderwidth=3)
e.grid(row=0,column=0 ,columnspan=7,padx=10,pady=10)

def setNumberAndOperation(sign):
    first_number = e.get()
    global f_num
    global operation
    operation = sign
    f_num = float(first_number)
    e.delete(0, END)
def factorial(n):
   if n == 1:return n
   return n*factorial(n-1)

def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0,str(current)+str(number))

def button_clear():
    e.delete(0, END)

def button_sqrt():
    setNumberAndOperation('sqrt')
    e.insert(0, math.sqrt(f_num))

def button_ln():
    setNumberAndOperation('ln')
    e.insert(0, math.log(f_num))


def button_factoriel():
    setNumberAndOperation('')
    e.insert(0, factorial(f_num))

def button_pow():
    setNumberAndOperation('')
    e.insert(0,f_num*f_num)

def button_log():
    setNumberAndOperation('ln')
    e.insert(0, math.log(f_num,10))

def button_pi():
    e.delete(0, END)
    e.insert(0, math.pi)


def button_equal():
        second_number = e.get()
        e.delete(0,END)
        if operation == '+':
            e.insert(0, f_num + float(second_number))
        elif operation == '-':
            e.insert(0, f_num - float(second_number))
        elif operation == '*':
            e.insert(0, f_num * float(second_number))
        elif operation == '/':
            e.insert(0, f_num / float(second_number))



button_1 = Button(root,text="1", padx=30,pady=10,command= lambda: button_click(1))
button_2 = Button(root,text="2", padx=30,pady=10,command= lambda: button_click(2))
button_3 = Button(root,text="3", padx=30,pady=10,command= lambda: button_click(3))
button_4 = Button(root,text="4", padx=30,pady=10,command= lambda: button_click(4))
button_5 = Button(root,text="5", padx=30,pady=10,command= lambda: button_click(5))
button_6 = Button(root,text="6", padx=30,pady=10,command= lambda: button_click(6))
button_7 = Button(root,text="7", padx=30,pady=10,command= lambda: button_click(7))
button_8 = Button(root,text="8", padx=30,pady=10,command= lambda: button_click(8))
button_9 = Button(root,text="9", padx=30,pady=10,command= lambda: button_click(9))
button_0 = Button(root,text="0", padx=30,pady=10,command= lambda: button_click(0))

button_add = Button(root,text="+", padx=30,pady=10,command=  lambda: setNumberAndOperation('+'))
button_substract = Button(root,text="-", padx=30,pady=10 ,command= lambda: setNumberAndOperation('-'))
button_multiply = Button(root,text="*", padx=30,pady=10,command= lambda: setNumberAndOperation('*'))
button_divide = Button(root,text="/", padx=30,pady=10,command= lambda: setNumberAndOperation('/'))

button_ln = Button(root,text="ln", padx=30,pady=10,command= button_ln)
button_log = Button(root,text="log", padx=30,pady=10,command= button_log)
button_pi = Button(root,text="π", padx=30,pady=10,command= button_pi)

button_pow = Button(root,text="x^2", padx=40,pady=20,command= button_pow)
button_factoriel = Button(root,text="n!", padx=40,pady=20,command= button_factoriel)



button_point = Button(root,text=".", padx=30,pady=10,command= lambda: button_click('.'))
button_sqrt = Button(root,text="√", padx=30,pady=10, command = button_sqrt)

button_equal = Button(root,text="=", padx=60,pady=20,command=  button_equal)
button_clear = Button(root,text="Clear", padx=60,pady=20,command=button_clear)


button_1.grid(row=3,column=0,sticky="nsew")
button_2.grid(row=3,column=1,sticky="nsew")
button_3.grid(row=3,column=2,sticky="nsew")

button_4.grid(row=2,column=0,sticky="nsew")
button_5.grid(row=2,column=1,sticky="nsew")
button_6.grid(row=2,column=2,sticky="nsew")

button_7.grid(row=1,column=0,sticky="nsew")
button_8.grid(row=1,column=1,sticky="nsew")
button_9.grid(row=1,column=2,sticky="nsew")

button_0.grid(row=4,column=0,sticky="nsew")

button_add.grid(row=4,column=3,sticky="nsew")
button_substract.grid(row=3,column=3,sticky="nsew")
button_multiply.grid(row=2,column=3,sticky="nsew")
button_divide.grid(row=1,column=3,sticky="nsew")

button_ln.grid(row=1,column=4,sticky="nsew")
button_log.grid(row=2,column=4,sticky="nsew")
button_pi.grid(row=3,column=4,sticky="nsew")
button_factoriel.grid(row=4,column=4,sticky="nsew")

button_point.grid(row=5,column=0,sticky="nsew")
button_sqrt.grid(row=5,column=3,sticky="nsew")
button_pow.grid(row=5,column=4,sticky="nsew")


button_clear.grid(row=5,column=1,columnspan=2,sticky="nsew")
button_equal.grid(row=4,column=1,columnspan=2,sticky="nsew")
root.mainloop()
