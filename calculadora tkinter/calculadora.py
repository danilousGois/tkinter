from tkinter import *


#colors 
background_color = "#2e2e2e"
display_color = "#131729"
numbers_buttons_color = "#9093a6"
font_numbers_buttons_color = "#25224a"
operators_buttons_color = "#0a0c40"
font_operators_buttons_color = "#ffffff"


#creating window
window = Tk()
window.title("Calculator")
window.geometry("240x375")
window.config(bg=background_color)


#ceating frames
display_frame = Frame(window, width=240, height=75, bg=display_color)
display_frame.grid(row=0, column=0)

buttons_frame = Frame(window, width=240, height=300)
buttons_frame.grid(row=1, column=0)


# creating actions

display_expression = StringVar()
all_values = ""

def calculate_expression():
    try:
        global all_values
        final_result = str(eval(all_values))
        display_expression.set(final_result)
        all_values = final_result
    except Exception:
        display_expression.set("Erro!")
        all_values = ""

def add_in_display(value):
    global all_values
    all_values = all_values + value
    display_expression.set(all_values)

def clear_display():
    global all_values
    all_values = ""
    display_expression.set(all_values)




#creating label
result_label = Label(display_frame, textvariable=display_expression, width=18, height=4, font=('Inter 16'), bg=display_color, fg=font_operators_buttons_color, anchor="e", padx=8, justify=RIGHT)
result_label.place(x=0, y=0)


#creating buttons

#row 1
button_1 = Button(buttons_frame, text="C", command=lambda: clear_display(), width=10, height=2, bg=operators_buttons_color, fg=font_operators_buttons_color, font=('Inter 15 bold'), )
button_1.place(x=0, y=0)

button_2 = Button(buttons_frame, text="%", command=lambda: add_in_display("%"), width=5, height=2, bg=operators_buttons_color, fg=font_operators_buttons_color, font=('Inter 15 bold'))
button_2.place(x=120, y=0)

button_3 = Button(buttons_frame, text="/", command=lambda: add_in_display("/"), width=5, height=2, bg=operators_buttons_color, fg=font_operators_buttons_color, font=('Inter 15 bold'))
button_3.place(x=180, y=0)

#row 2
button_4 = Button(buttons_frame, text="7", command=lambda: add_in_display("7"), width=5, height=2, bg=numbers_buttons_color, fg=font_numbers_buttons_color, font=('Inter 15 bold'))
button_4.place(x=0, y=60)

button_5 = Button(buttons_frame, text="8", command=lambda: add_in_display("8"), width=5, height=2, bg=numbers_buttons_color, fg=font_numbers_buttons_color, font=('Inter 15 bold'))
button_5.place(x=60, y=60)

button_6 = Button(buttons_frame, text="9", command=lambda: add_in_display("9"), width=5, height=2, bg=numbers_buttons_color, fg=font_numbers_buttons_color, font=('Inter 15 bold'))
button_6.place(x=120, y=60)

button_7 = Button(buttons_frame, text="*", command=lambda: add_in_display("*"), width=5, height=2, bg=operators_buttons_color, fg=font_operators_buttons_color, font=('Inter 15 bold'))
button_7.place(x=180, y=60)

#row 3
button_8 = Button(buttons_frame, text="4", command=lambda: add_in_display("4"), width=5, height=2, bg=numbers_buttons_color, fg=font_numbers_buttons_color, font=('Inter 15 bold'))
button_8.place(x=0, y=120)

button_9 = Button(buttons_frame, text="5", command=lambda: add_in_display("5"), width=5, height=2, bg=numbers_buttons_color, fg=font_numbers_buttons_color, font=('Inter 15 bold'))
button_9.place(x=60, y=120)

button_10 = Button(buttons_frame, text="6", command=lambda: add_in_display("6"), width=5, height=2, bg=numbers_buttons_color, fg=font_numbers_buttons_color, font=('Inter 15 bold'))
button_10.place(x=120, y=120)

button_11 = Button(buttons_frame, text="+", command=lambda: add_in_display("+"), width=5, height=2, bg=operators_buttons_color, fg=font_operators_buttons_color, font=('Inter 15 bold'))
button_11.place(x=180, y=120)

#row 4
button_12 = Button(buttons_frame, text="1", command=lambda: add_in_display("1"), width=5, height=2, bg=numbers_buttons_color, fg=font_numbers_buttons_color, font=('Inter 15 bold'))
button_12.place(x=0, y=180)

button_13 = Button(buttons_frame, text="2", command=lambda: add_in_display("2"), width=5, height=2, bg=numbers_buttons_color, fg=font_numbers_buttons_color, font=('Inter 15 bold'))
button_13.place(x=60, y=180)

button_14 = Button(buttons_frame, text="3", command=lambda: add_in_display("3"), width=5, height=2, bg=numbers_buttons_color, fg=font_numbers_buttons_color, font=('Inter 15 bold'))
button_14.place(x=120, y=180)

button_15 = Button(buttons_frame, text="-", command=lambda: add_in_display("-"), width=5, height=2, bg=operators_buttons_color, fg=font_operators_buttons_color, font=('Inter 15 bold'))
button_15.place(x=180, y=180)

#row 5
button_16 = Button(buttons_frame, text="0", command=lambda: add_in_display("0"), width=10, height=2, bg=numbers_buttons_color, fg=font_numbers_buttons_color, font=('Inter 15 bold'))
button_16.place(x=0, y=240)

button_17 = Button(buttons_frame, text=".", command=lambda: add_in_display("."), width=5, height=2, bg=numbers_buttons_color, fg=font_numbers_buttons_color, font=('Inter 15 bold'))
button_17.place(x=120, y=240)

button_18 = Button(buttons_frame, text="=", command=lambda: calculate_expression(), width=5, height=2, bg=operators_buttons_color, fg=font_operators_buttons_color, font=('Inter 15 bold'))
button_18.place(x=180, y=240)

window.mainloop()

# display_expression = ""