# INSTALLED LIBRARIES CurrencyConverter (pip install CurrencyConverter)
#  ENTER CURRENCY IN CAPITAL LETTERS ONLY 
from currency_converter import CurrencyConverter
import tkinter as tk
# available currencies
# EUR
# USD
# AUD
# etc 
# refer to https://www.countries-ofthe-world.com/world-currencies.html for more info i.e avout currencies
c = CurrencyConverter()
window = tk.Tk()
window.geometry("500x360")
window.title("sai's currency converter")

logo = tk.PhotoImage(file="nami.png")
logo_label = tk.Label(window, image=logo)
logo_label.place(x=10, y=10)

def clicked():
    amount = int(entry.get())
    cur1 = entry2.get()
    cur2 = entry3.get()
    data = c.convert(amount, cur1, cur2)
    label4 = tk.Label(window, text=data, font="Times 14 bold").place(x=190, y=300)
    label5 = tk.Label(window, text="result:", font="Times 14 bold").place(x=50, y=300)

label = tk.Label(window, text="Nami currency converter", font="Arial 20 bold").place(x=120, y=40)
label1 = tk.Label(window, text="Enter money:", font="Arial 15 bold").place(x=100, y=83)
entry = tk.Entry(window)
label2 = tk.Label(window, text="Enter currency:", font="Arial 15 bold").place(x=95, y=145)
entry2 = tk.Entry(window)
label3 = tk.Label(window, text="Enter currency u wanna change:", font="Arial 14 bold").place(x=5, y=195)
entry3 = tk.Entry(window)
button = tk.Button(window, text="submit", font="Times 15 bold", command=clicked).place(x=190, y=249)
entry.place(x=270, y=90)
entry2.place(x=270, y=150)
entry3.place(x=317, y=200)

window.mainloop()
