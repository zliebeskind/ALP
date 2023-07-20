import tkinter as tk

window = tk.Tk()
window.title("Calculator")
window.resizable(False, False)

frame = tk.Frame(window)
frame.grid(row=0, column=0, sticky="nsew")
window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(4, weight=1)
window.grid_columnconfigure(3, weight=1)

num = ""
operation = ""
box_text = []
state = 1

text_size = 24
font = "helvetica"

box_frame = tk.Frame(master=window, relief="sunken", borderwidth=4)
box_frame.grid(row=0, column=0, columnspan=5, sticky="n")
calc_box = tk.Label(master=box_frame, wraplength=250, text="".join(box_text), bg="white", height=2, width=16,
                    font=(font, text_size - 4))
calc_box.grid(row=0, column=0, columnspan=5, sticky="n")


def clicked_7():
    global box_text, calc_box
    box_text.append("7")
    calc_box.config(text="".join(box_text))


def clicked_8():
    global box_text, calc_box
    box_text.append("8")
    calc_box.config(text="".join(box_text))


def clicked_9():
    global box_text, calc_box
    box_text.append("9")
    calc_box.config(text="".join(box_text))


def clicked_4():
    global box_text, calc_box
    box_text.append("4")
    calc_box.config(text="".join(box_text))


def clicked_5():
    global box_text, calc_box
    box_text.append("5")
    calc_box.config(text="".join(box_text))


def clicked_6():
    global box_text, calc_box
    box_text.append("6")
    calc_box.config(text="".join(box_text))


def clicked_1():
    global box_text, calc_box
    box_text.append("1")
    calc_box.config(text="".join(box_text))


def clicked_2():
    global box_text, calc_box
    box_text.append("2")
    calc_box.config(text="".join(box_text))


def clicked_3():
    global box_text, calc_box
    box_text.append("3")
    calc_box.config(text="".join(box_text))


def clicked_0():
    global box_text, calc_box
    box_text.append("0")
    calc_box.config(text="".join(box_text))


def clicked_point():
    global box_text, calc_box
    if "." not in box_text:
        box_text.append(".")
        calc_box.config(text="".join(box_text))


def clicked_negative():
    global box_text, calc_box
    if not box_text:
        box_text.append("-")
        calc_box.config(text="".join(box_text))


def add():
    global box_text, num, state, calc_box, operation
    if box_text and box_text != ["-"] and box_text != ["."]:
        if state == 2:
            equals()
        num = float("".join(box_text))
        state = 2
        operation = "+"
        box_text = []
        calc_box.config(text="")


def subtract():
    global box_text, num, state, calc_box, operation
    if box_text and box_text != ["-"] and box_text != ["."]:
        if state == 2:
            equals()
        num = float("".join(box_text))
        state = 2
        operation = "-"
        box_text = []
        calc_box.config(text="")


def multiply():
    global box_text, num, state, calc_box, operation
    if box_text and box_text != ["-"] and box_text != ["."]:
        if state == 2:
            equals()
        num = float("".join(box_text))
        state = 2
        operation = "*"
        box_text = []
        calc_box.config(text="")


def divide():
    global box_text, num, state, calc_box, operation
    if box_text and box_text != ["-"] and box_text != ["."]:
        if state == 2:
            equals()
        num = float("".join(box_text))
        state = 2
        operation = "/"
        box_text = []
        calc_box.config(text="")


def equals():
    global num, operation, box_text, state, calc_box
    if state == 2 and box_text and box_text != ["-"] and box_text != ["."]:
        if operation == "+":
            num += float("".join(box_text))
        if operation == "-":
            num -= float("".join(box_text))
        if operation == "*":
            num *= float("".join(box_text))
        if operation == "/":
            num /= float("".join(box_text))
        box_text = [*str(num)]
        calc_box.config(text=str(num))
        state = 1


def clear():
    global num, operation, box_text, state, calc_box
    num = ""
    operation = ""
    box_text = []
    state = 1
    calc_box.config(text="")


button_7 = tk.Button(text="7", height=1, width=3, font=(font, text_size), command=clicked_7)
button_7.grid(row=1, column=0, sticky="n")

button_8 = tk.Button(text="8", height=1, width=3, font=(font, text_size), command=clicked_8)
button_8.grid(row=1, column=1, sticky="n")

button_9 = tk.Button(text="9", height=1, width=3, font=(font, text_size), command=clicked_9)
button_9.grid(row=1, column=2, sticky="n")

button_4 = tk.Button(text="4", height=1, width=3, font=(font, text_size), command=clicked_4)
button_4.grid(row=2, column=0, sticky="n")

button_5 = tk.Button(text="5", height=1, width=3, font=(font, text_size), command=clicked_5)
button_5.grid(row=2, column=1, sticky="n")

button_6 = tk.Button(text="6", height=1, width=3, font=(font, text_size), command=clicked_6)
button_6.grid(row=2, column=2, sticky="n")

button_1 = tk.Button(text="1", height=1, width=3, font=(font, text_size), command=clicked_1)
button_1.grid(row=3, column=0, sticky="n")

button_2 = tk.Button(text="2", height=1, width=3, font=(font, text_size), command=clicked_2)
button_2.grid(row=3, column=1, sticky="n")

button_3 = tk.Button(text="3", height=1, width=3, font=(font, text_size), command=clicked_3)
button_3.grid(row=3, column=2, sticky="n")

button_0 = tk.Button(text="0", height=1, width=3, font=(font, text_size), command=clicked_0)
button_0.grid(row=4, column=0, sticky="n")

button_point = tk.Button(text=".", height=1, width=3, font=(font, text_size), command=clicked_point)
button_point.grid(row=4, column=1, sticky="n")

button_negative = tk.Button(text="(-)", height=1, width=3, font=(font, text_size), command=clicked_negative)
button_negative.grid(row=4, column=2, sticky="n")

button_add = tk.Button(text="+", height=1, width=3, font=(font, text_size), command=add)
button_add.grid(row=1, column=4, sticky="n")

button_subtract = tk.Button(text="\u2212", height=1, width=3, font=(font, text_size), command=subtract)
button_subtract.grid(row=2, column=4, sticky="n")

button_multiply = tk.Button(text="\u00d7", height=1, width=3, font=(font, text_size), command=multiply)
button_multiply.grid(row=3, column=4, sticky="n")

button_divide = tk.Button(text="\u00f7", height=1, width=3, font=(font, text_size), command=divide)
button_divide.grid(row=4, column=4, sticky="n")

button_clear = tk.Button(text="CC", height=1, width=6, font=(font, text_size + 3), command=clear)
button_clear.grid(row=5, column=0, columnspan=2)

button_equals = tk.Button(text="=", height=1, width=6, font=(font, text_size + 3), command=equals)
button_equals.grid(row=5, column=2, columnspan=4)

window.mainloop()
