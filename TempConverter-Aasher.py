# Developed by Aasher
from tkinter import *
from tkinter.ttk import Combobox

#--------Variables------------
select_value = ('Celsius', 'Fahrenheit', 'Kelvin')
from_symbol = None
to_symbol = None
in_value = 0
out_value = 0

#--------Functions------------
def in_temp():
    global from_symbol, to_symbol, in_value
    from_symbol = (from_combo.get()).capitalize()
    to_symbol = (to_combo.get()).capitalize()
    in_value = input_temp.get()

    try:
        in_value = float(in_value)
    except ValueError:
        output_temp.config(text="Invalid Input", fg='#c93434')
    finally:
        pass

    if from_symbol != 'Celsius' and from_symbol != 'Fahrenheit' and from_symbol != 'Kelvin':
        output_temp.config(text="Invalid Input", fg='#c93434')
    elif to_symbol != 'Celsius' and to_symbol != 'Fahrenheit' and to_symbol != 'Kelvin':
        output_temp.config(text="Invalid Input", fg='#c93434')

    update_temp()

def update_temp():
    global out_value

    if from_symbol == to_symbol:
        out_value = in_value
        output_temp.config(text=f"{out_value:.2f}", fg='#969696')

    elif from_symbol == 'Celsius' and to_symbol == 'Fahrenheit':
        out_value = (9/5) * in_value + 32.0
        output_temp.config(text=f"{out_value:.2f}", fg='#969696')

    elif from_symbol == 'Celsius' and to_symbol == 'Kelvin':
        out_value = in_value + 273.15
        output_temp.config(text=f"{out_value:.2f}", fg='#969696')

    elif from_symbol == 'Fahrenheit' and to_symbol == 'Celsius':
        out_value = (in_value - 32) * 5/9
        output_temp.config(text=f"{out_value:.2f}", fg='#969696')

    elif from_symbol == 'Fahrenheit' and to_symbol == 'Kelvin':
        out_value = (in_value - 32) * 5/9 + 273.15
        output_temp.config(text=f"{out_value:.2f}", fg='#969696')

    elif from_symbol == 'Kelvin' and to_symbol == 'Celsius':
        out_value = in_value - 273.15
        output_temp.config(text=f"{out_value:.2f}", fg='#969696')

    elif from_symbol == 'Kelvin' and to_symbol == 'Fahrenheit':
        out_value = (in_value - 273.15) * 1.8 + 32.0
        output_temp.config(text=f"{out_value:.2f}", fg='#969696')

#---------Window--------------
window = Tk()

window.geometry("515x550")
window.resizable(False, False)
window.config(bg="#1d1f1d")
window.title("Temperature Converter - Aasher_Elahi")

#---------------------------
heading = Label(window, text="Temperature Interconverter",
                font=("Arial Rounded MT Bold", 24, 'bold'),
                fg="#edf0ed", bg="#292929",
                relief=GROOVE, bd=1, padx=40, pady=13)
heading.pack(side='top')

#------------------------------
back_box1 = Label(window, text="       ", fg="#edf0ed",
               bg="#1d1f1d", relief=GROOVE, bd=1, padx=239, pady=110)
back_box1.place(x=7, y=86)

#------------------------------
back_box2 = Label(window, text="       ", fg="#edf0ed",
               bg="#1d1f1d", relief=RIDGE, bd=1, padx=239, pady=90)
back_box2.place(x=7, y=346)

#------------------------------
text_box1 = Label(window,
               text="Input",
               font=("Arial Rounded MT Bold", 16),
               relief=GROOVE, bd=1, padx=13, pady=5,
               fg="#2abf2a", bg="#1d1f1d")
text_box1.place(x=23, y=70)

#------------------------------
text_box2 = Label(window,
               text="Output",
               font=("Arial Rounded MT Bold", 16),
               relief=GROOVE, bd=1, padx=13, pady=5,
               fg="#c93434", bg="#1d1f1d")
text_box2.place(x=23, y=330)

#-------------------------------
t_from = Label(window,
               text="Convert from :",
               font=("Arial Rounded MT Bold", 14),
               fg="#edf0ed", bg="#1d1f1d")
t_from.place(x=86, y=130)

#--------------------------------
t_to = Label(window,
               text="Convert to :",
               font=("Arial Rounded MT Bold", 14),
               fg="#edf0ed", bg="#1d1f1d")
t_to.place(x=86, y=175)

#--------------------------------
t_value = Label(window,
               text="Enter the temperature to be convert ↓↓",
               font=("Arial Rounded MT Bold", 14),
               fg="#edf0ed", bg="#1d1f1d")
t_value.place(x=86, y=220)

#--------------------------------
from_combo = Combobox(window, values=select_value,
                      font=("Arial Rounded MT", 12))
from_combo.set('Select')
from_combo.place(x=238, y=133)

#--------------------------------
to_combo = Combobox(window, values=select_value,
                      font=("Arial Rounded MT", 12))
to_combo.set('Select')
to_combo.place(x=238, y=178)

#------------------------------
input_temp = Entry(window, font=("consolas", 17),
                   fg="#ededed", bg="#292929",
                   relief=RIDGE, width=20)
input_temp.place(x= 86, y=260)

#------------------------------
output_temp = Label(window,
               text="000.00",
               font=("Arial Rounded MT Bold", 40),
               fg="#969696", bg="#1d1f1d")
output_temp.pack(side='bottom', pady=72)
#--------------------------------
convert_button = Button(window, text='Convert ✅',
                        bg="#292929", fg="white",
                        font=("Arial Rounded MT Bold", 11),
                        relief=RIDGE, height=1,
                        activeforeground="White", activebackground="#292929",
                        command=in_temp)
convert_button.place(x=349, y=260)

#------------------------------
window.mainloop()

# all right reserved. Owned by Tabassat and Aasher's team.