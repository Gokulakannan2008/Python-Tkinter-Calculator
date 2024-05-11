#*****************************#*****************************#*****************************#
#                             #                                                           #
#     Tkinter  Calculator     #                                                           #
#                             #                                                           #
#                             #                                                           #
#*****************************#                          WELCOME                          #
#                             #                                                           #
#    Gokulakannan P           #                                                           #
#    Python Programmer        #                                                           #
#                             #                                                           #
#*****************************#*****************************#*****************************#


from tkinter import *
from tkinter.font import Font
from tkinter import messagebox

root = Tk()
root.state("zoomed")
root.title("Calculator")


c = StringVar()


font1 = Font(root, family="Ariel", size=40, weight="bold")


frame1 = Frame(root, bg="light green")
frame1.pack(fill=X, side=TOP)


label1 = Label(frame1, text="", font=("sans-serif", 89, "bold"), bg="Light green")
label1.grid(row=0, column=0, columnspan=9)


enter =Entry(frame1, font=font1, textvariable=c, width=53)
enter.configure(justify="right", relief=SOLID)
enter.grid(row=1, column=0)


def calculate():
    try:
         result = eval(c.get())
         c.set("")
         c.set(result)
    except Exception as e:
        c.set("")
        messagebox.showerror("Syntax Error", "Invalid syntax")


def backspace(event):
    if event.keysym == "BackSpace":
        entry_text = c.get()
        entry_text = entry_text[:-1]
        c.delete(0, END)
        c.insert(0, entry_text)



current_value = enter.get()
enter.delete(0, END)

def update_entry(value):
    enter.insert(END,current_value + value)


def _1():
    update_entry("1")


def _2():
    update_entry("2")


def _3():
    update_entry("3")


def _4():
    update_entry("4")


def _5():
    update_entry("5")


def _6():
    update_entry("6")


def _7():
    update_entry("7")


def _8():
    update_entry("8")


def _9():
    update_entry("9")

def _0():
    update_entry("0")


def _subraction():
    update_entry("-")


def _divide():
    update_entry("/")


def _add():
    update_entry("+")


def _multiplication():
    update_entry("*")


def _backspace():
    entry_text = enter.get()
    entry_text = entry_text[:-1]
    enter.delete(0, END)
    enter.insert(0, entry_text)


def _clear():
    c.set("")


def _equal():
    try:
         result = eval(c.get())
         c.set("")
         c.set(result)
    except Exception as e:
        c.set("")
        messagebox.showerror("Syntax Error", "Invalid syntax")



frame2 = Frame(frame1, bg="light green", border=3)
frame2.grid(row=2, column=0)

button1 = Button(frame2, text="1", width=30, height=5, bg="grey", fg="BLACK", border=3,
                activebackground="light grey", activeforeground="Black", font=("ariel black", 10, "bold"), command=_1)
button1.config(relief=SOLID)
button1.grid(row=0, column=0, sticky=E, padx=10, pady=10)

button2 =Button(frame2, text="2", width=30, height=5, bg="grey", fg="BLACK", border=3,
                activebackground="light grey", activeforeground="Black", font=("ariel black", 10, "bold"), command=_2)
button2.config(relief=SOLID)
button2.grid(row=0, column=1, sticky=E, padx=10, pady=10)


button3 = Button(frame2, text="3", width=30, height=5, bg="grey", fg="BLACK", border=3,
                activebackground="light grey", activeforeground="Black", font=("ariel black", 10, "bold"), command=_3)
button3.config(relief=SOLID)
button3.grid(row=0, column=2, sticky=E, padx=10, pady=10)


button4 = Button(frame2, text="4", width=30, height=5, bg="grey", fg="BLACK", border=3,
                activebackground="light grey", activeforeground="Black", font=("ariel black", 10, "bold"), command=_4)
button4.config(relief=SOLID)
button4.grid(row=0, column=3, sticky=E, padx=10, pady=10)


button5 = Button(frame2, text="5", width=30, height=5, bg="grey", fg="BLACK", border=3,
                activebackground="light grey", activeforeground="Black", font=("ariel black", 10, "bold"), command=_5)
button5.config(relief=SOLID)
button5.grid(row=1, column=0, sticky=E, padx=10, pady=10)


button6 = Button(frame2, text="6", width=30, height=5, bg="grey", fg="BLACK", border=3,
                activebackground="light grey", activeforeground="Black", font=("ariel black", 10, "bold"), command=_6)
button6.config(relief=SOLID)
button6.grid(row=1, column=1, sticky=E, padx=10, pady=10)


button7 = Button(frame2, text="7", width=30, height=5, bg="grey", fg="BLACK", border=3,
                activebackground="light grey", activeforeground="Black", font=("ariel black", 10, "bold"), command=_7)
button7.config(relief=SOLID)
button7.grid(row=1, column=2, sticky=E, padx=10, pady=10)


button8 = Button(frame2, text="8", width=30, height=5, bg="grey", fg="BLACK", border=3,
                activebackground="light grey", activeforeground="Black", font=("ariel black", 10, "bold"), command=_8)
button8.config(relief=SOLID)
button8.grid(row=1, column=3, sticky=E, padx=10, pady=10)


button9 = Button(frame2, text="9", width=30, height=5, bg="grey", fg="BLACK", border=3,
                activebackground="light grey", activeforeground="Black", font=("ariel black", 10, "bold"), command=_9)
button9.config(relief=SOLID)
button9.grid(row=2, column=0, sticky=E, padx=10, pady=10)


button0 = Button(frame2, text="0", width=30, height=5, bg="grey", fg="BLACK", border=3,
                activebackground="light grey", activeforeground="Black", font=("ariel black", 10, "bold"), command=_0)
button0.config(relief=SOLID)
button0.grid(row=2, column=1, sticky=E, padx=10, pady=10)


buttonadd = Button(frame2, text="+", width=30, height=5, bg="grey", fg="BLACK", border=3,
                activebackground="light grey", activeforeground="Black", font=("ariel black", 10, "bold"), command=_add)
buttonadd.config(relief=SOLID)
buttonadd.grid(row=2, column=2, sticky=E, padx=10, pady=10)

buttonsub = Button(frame2, text="-", width=30, height=5, bg="grey", fg="BLACK", border=3,
                activebackground="light grey", activeforeground="Black", font=("ariel black", 10, "bold"), command=_subraction)
buttonsub.config(relief=SOLID)
buttonsub.grid(row=2, column=3, sticky=E, padx=10, pady=10)


buttonmulti = Button(frame2, text="X", width=30, height=5, bg="grey", fg="BLACK", border=3,
                activebackground="light grey", activeforeground="Black", font=("ariel black", 10, "bold"), command=_multiplication)
buttonmulti.config(relief=SOLID)
buttonmulti.grid(row=3, column=0, sticky=E, padx=10, pady=10)


buttondivide = Button(frame2, text="/", width=30, height=5, bg="grey", fg="BLACK", border=3,
                activebackground="light grey", activeforeground="Black", font=("ariel black", 10, "bold"), command=_divide)
buttondivide.config(relief=SOLID)
buttondivide.grid(row=3, column=1, sticky=E, padx=10, pady=10)

buttonback = Button(frame2, text="Backspase", width=30, height=5, bg="grey", fg="BLACK", border=3,
                activebackground="light grey", activeforeground="Black", font=("ariel black", 10, "bold"), command=_backspace)
buttonback.config(relief=SOLID)
buttonback.grid(row=3, column=2, sticky=E, padx=10, pady=10)


buttonclear = Button(frame2, text="CE", width=30, height=5, bg="grey", fg="BLACK", border=3,
                activebackground="light grey", activeforeground="Black", font=("ariel black", 10, "bold"), command=_clear)
buttonclear.config(relief=SOLID)
buttonclear.grid(row=3, column=3, sticky=E, padx=10, pady=10)


buttonequal = Button(frame2, text="=", height=5, width=132, bg="grey", fg="BLACK", border=3,
                activebackground="light grey", activeforeground="Black", font=("ariel black", 10, "bold"), command=_equal)
buttonequal.config(relief=SOLID)
buttonequal.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

enter.bind("<Return>", lambda event: calculate())
enter.bind("<KeyPress>", backspace)

root.mainloop()
