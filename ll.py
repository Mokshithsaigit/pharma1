import tkinter as tk
x=0
root = tk.Tk()
root.geometry("400x400")

# Create the widgets
name_label = tk.Label(root, text="Student Name:")
name_entry = tk.Entry(root)
name_entry.insert(0, "-")

roll_label = tk.Label(root, text="Roll No:")
roll_entry = tk.Entry(root)
roll_entry.insert(0, "0")

phone_label = tk.Label(root, text="Phone No:")
phone_entry = tk.Entry(root)
phone_entry.insert(0, "0")

marks1_label = tk.Label(root, text="Marks 1:")
marks1_entry = tk.Entry(root)
marks1_entry.insert(0, "0")

marks2_label = tk.Label(root, text="Marks 2:")
marks2_entry = tk.Entry(root)
marks2_entry.insert(0, "0")

total_label = tk.Label(root, text="Total Marks:")
total_entry = tk.Entry(root)


def calculate_total():
    # Get the values of marks1_entry and marks2_entry
    global x
    marks1 = int(marks1_entry.get())
    marks2 = int(marks2_entry.get())

    # Calculate the total and update total_entry
    total = marks1 + marks2
    total_entry.delete(0, tk.END)
    total_entry.insert(0, total)
    x = total
    print(x)


# Create the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_total)



# Add the widgets to the window
name_label.pack()
name_entry.pack()

roll_label.pack()
roll_entry.pack()

phone_label.pack()
phone_entry.pack()

marks1_label.pack()
marks1_entry.pack()

marks2_label.pack()
marks2_entry.pack()

total_label.pack()
total_entry.pack()

calculate_button.pack()

root.mainloop()

