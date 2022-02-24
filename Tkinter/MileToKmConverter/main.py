import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)
km = 0
mile = 0


def convert_miles_to_km():
    result = int(text_box.get()) * 1.6
    label_2.config(text=f"{result}")


# label 1
label_1 = tkinter.Label(text="is equal to", font=("Arial", 20))
label_1.grid(column=0, row=1)

# label 2
label_2 = tkinter.Label(text=f"{km}", font=("Arial", 20), width=15)
label_2.grid(column=1, row=1)

# label 3
label_3 = tkinter.Label(text="Km", font=("Arial", 20))
label_3.grid(column=2, row=1)

# label 4
label_4 = tkinter.Label(text="Miles", font=("Arial", 20))
label_4.grid(column=2, row=0)

# button
button = tkinter.Button(text="Calculate", command=convert_miles_to_km)
button.grid(column=1, row=2)
# Entry
text_box = tkinter.Entry(window, width=10)
text_box.insert(0, f"{mile}")
text_box.grid(column=1, row=0)




window.mainloop()
