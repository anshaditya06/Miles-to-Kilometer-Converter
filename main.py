from tkinter import *

# Window
window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)

# Entry
entry = Entry(window, width=10)
print(entry.get())
entry.grid(column=0, row=0)

# Label/Text
label = Label(window, text="Miles", font=("Arial", 20))
label.grid(column=1, row=0)


# Button
button = Button(window, text="Convert", font=("Arial", 15))
button.grid(column=2, row=2)


# Kilometer Label
km_label = Label(window, text="Km", font=("Arial", 20))
km_label.grid(column=4, row=0)



# Result
result_label = Label(window, text="")
result_label.grid(column=3, row=0)


def convert():
      miles= float(entry.get())
      kilometer = miles * 1.609
      km  = round(kilometer, 2)
      result_label.config(text=f"{km}", font=("Arial", 20))

button.config(command=convert)


window.mainloop()


