import tkinter as tk


def miles_to_km():
    miles = float(insert_mile.get())
    result = miles * 1.609
    result_label.config(text=f"{result}")


window = tk.Tk()
window.title("Miles to Km Converter")
window.config(padx=10, pady=10)

# Label
is_equal_to_label = tk.Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)
# Entry for insert mile
insert_mile = tk.Entry(width=5)
insert_mile.grid(column=1, row=0)
# Label Mile
mile_label = tk.Label(text="Miles")
mile_label.grid(column=2, row=0)
# Label result
result_label = tk.Label(text="0")
result_label.grid(column=1, row=1)

# Label Km
km = tk.Label(text="Km")
km.grid(column=2, row=1)
# Button
button = tk.Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=3)

window.mainloop()
