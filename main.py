from tkinter import *
import csv
import datetime
from PIL import ImageTk, Image
import pandas as pd
from tkinter import messagebox
import re
import matplotlib.pyplot as plt

root = Tk()
root.geometry("900x600")
root.maxsize(900, 600)
root.minsize(900, 600)
root.title("True Pharma's")
bg = PhotoImage(file=r"C:\Users\Lenovo\Downloads\main.png")
c1 = Canvas(root, width=900, height=600)
c1.pack(fill="both", expand=False)
c1.create_image(0, 0, image=bg, anchor="nw")
c1.create_text(450, 120, text="True PHarma", font=('serif', 70, 'bold'),fill="#99FF99")


def sell():
    global bg1
    top1 = Toplevel(root)
    top1.geometry('900x600')
    top1.maxsize(900, 600)
    top1.minsize(900, 600)

    bg1 = PhotoImage(file=r"C:\Users\Lenovo\Downloads\sell21.png")
    ca1 = Canvas(top1, width=900, height=600)
    ca1.pack(fill='both', expand=True)
    ca1.create_image(0, 0, image=bg1, anchor="nw")
    ca1.create_text(435, 35, text="Selling Page", font=('Helvetica', 23, 'bold'), fill='#FF3333')

    ca1.create_text(90, 100, text="Customer Name", font=('Arial', 14, 'bold'), fill='#FFFFFF')
    ca1.create_text(600, 100, text="Customer E-mail", font=('Arial', 14, 'bold'), fill='#FFFFFF')

    ca1.create_text(100, 150, text="Medicine Details:-", font=('Arial', 14, 'bold'), fill='#FFFFFF')
    ca1.create_text(30, 230, text="1.", font=('Arial', 14, 'bold'), fill='#FFFFFF')
    ca1.create_text(30, 270, text="2.", font=('Arial', 14, 'bold'), fill='#FFFFFF')
    ca1.create_text(30, 310, text="3.", font=('Arial', 14, 'bold'), fill='#FFFFFF')
    ca1.create_text(30, 350, text="4.", font=('Arial', 14, 'bold'), fill='#FFFFFF')
    ca1.create_text(30, 390, text="5.", font=('Arial', 14, 'bold'), fill='#FFFFFF')

    ca1.create_text(170, 180, text="Medicine Name", font=('Arial', 14, 'bold'), fill='#FFFFFF')
    # ca1.create_text(100, 150, text="Type", font=('Arial', 14, 'bold'), fill='#FFFFFF')
    ca1.create_text(350, 180, text="Quantity", font=('Arial', 14, 'bold'), fill='#FFFFFF')
    ca1.create_text(530, 180, text="Price", font=('Arial', 14, 'bold'), fill='#FFFFFF')
    ca1.create_text(760, 180, text="Total Price", font=('Arial', 14, 'bold'), fill='#FFFFFF')

    def clear_entry(event, entry):
        if entry.get() == entry.get().split()[0] if len(entry.get().split()) > 0 else entry.get():
            entry.delete(0, "end")
    global e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14,e15,e16,e17,e18,e19,e20,e21,e22,e23,e24,e25,e26
    e1 = Entry(top1, width=25)
    e1.insert(0, "-")
    e1.bind("<FocusIn>", lambda event: clear_entry(event, e1))
    e1.place(x=190, y=93)
    e2 = Entry(top1, width=25)
    e2.insert(0, "-")
    e2.bind("<FocusIn>", lambda event: clear_entry(event, e2))
    e2.place(x=700, y=93)

    e3 = Entry(top1, width=25)
    e3.insert(0, "-")
    e3.bind("<FocusIn>", lambda event: clear_entry(event, e3))
    e3.place(x=90, y=220)
    e4 = Entry(top1, width=25)
    e4.insert(0, "0")
    e4.bind("<FocusIn>", lambda event: clear_entry(event, e4))
    e4.place(x=290, y=220)
    e5 = Entry(top1, width=25)
    e5.insert(0, "0")
    e5.bind("<FocusIn>", lambda event: clear_entry(event, e5))
    e5.place(x=490, y=220)

    e6 = Entry(top1, width=25)
    e6.insert(0, "-")
    e6.bind("<FocusIn>", lambda event: clear_entry(event, e6))
    e6.place(x=90, y=260)
    e7 = Entry(top1, width=25)
    e7.insert(0, "0")
    e7.bind("<FocusIn>", lambda event: clear_entry(event, e7))
    e7.place(x=290, y=260)
    e8 = Entry(top1, width=25)
    e8.insert(0, "0")
    e8.bind("<FocusIn>", lambda event: clear_entry(event, e8))
    e8.place(x=490, y=260)

    e9 = Entry(top1, width=25)
    e9.insert(0, "-")
    e9.bind("<FocusIn>", lambda event: clear_entry(event, e9))
    e9.place(x=90, y=300)
    e10 = Entry(top1, width=25)
    e10.insert(0, "0")
    e10.bind("<FocusIn>", lambda event: clear_entry(event, e10))
    e10.place(x=290, y=300)
    e11 = Entry(top1, width=25)
    e11.insert(0, "0")
    e11.bind("<FocusIn>", lambda event: clear_entry(event, e11))
    e11.place(x=490, y=300)

    e12 = Entry(top1, width=25)
    e12.insert(0, "-")
    e12.bind("<FocusIn>", lambda event: clear_entry(event, e12))
    e12.place(x=90, y=340)
    e13 = Entry(top1, width=25)
    e13.insert(0, "0")
    e13.bind("<FocusIn>", lambda event: clear_entry(event, e13))
    e13.place(x=290, y=340)
    e14 = Entry(top1, width=25)
    e14.insert(0, "0")
    e14.bind("<FocusIn>", lambda event: clear_entry(event, e14))
    e14.place(x=490, y=340)

    e15 = Entry(top1, width=25)
    e15.insert(0, "-")
    e15.bind("<FocusIn>", lambda event: clear_entry(event, e15))
    e15.place(x=90, y=380)
    e16 = Entry(top1, width=25)
    e16.insert(0, "0")
    e16.bind("<FocusIn>", lambda event: clear_entry(event, e16))
    e16.place(x=290, y=380)
    e17 = Entry(top1, width=25)
    e17.insert(0, "0")
    e17.bind("<FocusIn>", lambda event: clear_entry(event, e17))
    e17.place(x=490, y=380)

    e18 = Entry(top1, width=25)
    e18.insert(0, "0")
    e18.place(x=690, y=420)


    #Total section

    e19 = Entry(top1, width=25)
    e19.insert(0, "0")
    e19.place(x=690, y=220)

    e20 = Entry(top1, width=25)
    e20.insert(0, "0")
    e20.place(x=690, y=260)

    e21 = Entry(top1, width=25)
    e21.insert(0, "0")
    e21.place(x=690, y=300)

    e22 = Entry(top1, width=25)
    e22.insert(0, "0")
    e22.place(x=690, y=340)

    e23 = Entry(top1, width=25)
    e23.insert(0, "0")
    e23.place(x=690, y=380)
    def check():
        usi1 = e1.get()
        usi2 = e2.get()
        usi3 = e3.get()
        usi4 = e4.get()
        usi5 = e5.get()
        usi6 = e6.get()
        usi7 = e7.get()
        usi8 = e8.get()
        usi9 = e9.get()
        usi10 = e10.get()
        usi11 = e11.get()
        usi12 = e12.get()
        usi13 = e13.get()
        usi14 = e14.get()
        usi15 = e15.get()
        usi16 = e16.get()
        usi17 = e17.get()
        count = 0

        try:
            # Check if input value only contains alphabets using regex
            if not re.match("^[a-zA-Z-.]+$", usi1):
                raise ValueError
            else:
                count = count +1

        except ValueError:
            # If input is invalid, display error message and destroy after 1 sec
            message_label = Label(top1, text="Input is invalid!", fg="#FF3333",bg="#E0E0E0",font=("Arial",10))
            message_label.place(x=220, y=120)
            message_label.after(1000, lambda: message_label.destroy())

        try:
            # Check if input value only contains alphabets using regex
            if not re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", usi2):
                raise ValueError
            else:
                count = count +1

        except ValueError:
            # If input is invalid, display error message and destroy after 1 sec
            message_label2 = Label(top1, text="Input is invalid!", fg="#FF3333",bg="#E0E0E0",font=("Arial",10))
            message_label2.place(x=725, y=120)
            message_label2.after(1000, lambda: message_label2.destroy())

        try:
            # Check if input value only contains alphabets using regex
            if not re.match("^[a-zA-Z-]+$", usi3):
                raise ValueError
            else:
                count = count +1

        except ValueError:
            # If input is invalid, display error message and destroy after 1 sec
            message_label3 = Label(top1, text="Input is invalid!", fg="#FF3333",bg="#E0E0E0",font=("Arial",7))
            message_label3.place(x=130, y=240)
            message_label3.after(1000, lambda: message_label3.destroy())

        try:
            # Check if input value only contains alphabets using regex
            if not re.match("^[a-zA-Z-]+$", usi6):
                raise ValueError
            else:
                count = count +1

        except ValueError:
            # If input is invalid, display error message and destroy after 1 sec
            message_label6 = Label(top1, text="Input is invalid!", fg="#FF3333",bg="#E0E0E0",font=("Arial",7))
            message_label6.place(x=130, y=280)
            message_label6.after(1000, lambda: message_label6.destroy())

        try:
            # Check if input value only contains alphabets using regex
            if not re.match("^[a-zA-Z-]+$", usi9):
                raise ValueError
            else:
                count = count +1

        except ValueError:
            # If input is invalid, display error message and destroy after 1 sec
            message_label9 = Label(top1, text="Input is invalid!", fg="#FF3333",bg="#E0E0E0",font=("Arial",7))
            message_label9.place(x=130, y=320)
            message_label9.after(1000, lambda: message_label9.destroy())

        try:
            # Check if input value only contains alphabets using regex
            if not re.match("^[a-zA-Z-]+$", usi12):
                raise ValueError
            else:
                count = count +1

        except ValueError:
            # If input is invalid, display error message and destroy after 1 sec
            message_label12 = Label(top1, text="Input is invalid!", fg="#FF3333",bg="#E0E0E0",font=("Arial",7))
            message_label12.place(x=130, y=360)
            message_label12.after(1000, lambda: message_label12.destroy())

        try:
            # Check if input value only contains alphabets using regex
            if not re.match("^[a-zA-Z-]+$", usi15):
                raise ValueError
            else:
                count = count +1

        except ValueError:
            # If input is invalid, display error message and destroy after 1 sec
            message_label15 = Label(top1, text="Input is invalid!", fg="#FF3333",bg="#E0E0E0",font=("Arial",7))
            message_label15.place(x=130, y=400)
            message_label15.after(1000, lambda: message_label15.destroy())

        try:
                # Check if input value only contains alphabets using regex
            if not re.match("^[0-9]+$", usi4):
                    raise ValueError
            else:
                count = count +1
        except ValueError:
                # If input is invalid, display error message and destroy after 1 sec
                message_label4 = Label(top1, text="Input is invalid!", fg="#FF3333",bg="#E0E0E0",font=("Arial",7))
                message_label4.place(x=320, y=240)
                message_label4.after(1000, lambda: message_label4.destroy())

        try:
                # Check if input value only contains alphabets using regex
            if not re.match("^[0-9]+$", usi5):
                    raise ValueError
            else:
                count = count +1
        except ValueError:
                # If input is invalid, display error message and destroy after 1 sec
                message_label5 = Label(top1, text="Input is invalid!", fg="#FF3333",bg="#E0E0E0",font=("Arial",7))
                message_label5.place(x=520, y=240)
                message_label5.after(1000, lambda: message_label5.destroy())

        try:
                # Check if input value only contains alphabets using regex
            if not re.match("^[0-9]+$", usi7):
                    raise ValueError
            else:
                count = count +1
        except ValueError:
                # If input is invalid, display error message and destroy after 1 sec
                message_label7 = Label(top1, text="Input is invalid!", fg="#FF3333",bg="#E0E0E0",font=("Arial",7))
                message_label7.place(x=320, y=280)
                message_label7.after(1000, lambda: message_label7.destroy())

        try:
                # Check if input value only contains alphabets using regex
            if not re.match("^[0-9]+$", usi8):
                    raise ValueError
            else:
                count = count +1
        except ValueError:
                # If input is invalid, display error message and destroy after 1 sec
                message_label8 = Label(top1, text="Input is invalid!", fg="#FF3333",bg="#E0E0E0",font=("Arial",7))
                message_label8.place(x=520, y=280)
                message_label8.after(1000, lambda: message_label8.destroy())

        try:
                # Check if input value only contains alphabets using regex
            if not re.match("^[0-9]+$", usi10):
                    raise ValueError
            else:
                count = count +1
        except ValueError:
                # If input is invalid, display error message and destroy after 1 sec
                message_label10 = Label(top1, text="Input is invalid!", fg="#FF3333",bg="#E0E0E0",font=("Arial",7))
                message_label10.place(x=320, y=320)
                message_label10.after(1000, lambda: message_label10.destroy())

        try:
                # Check if input value only contains alphabets using regex
            if not re.match("^[0-9]+$", usi11):
                    raise ValueError
            else:
                count = count +1
        except ValueError:
                # If input is invalid, display error message and destroy after 1 sec
                message_label11 = Label(top1, text="Input is invalid!", fg="#FF3333",bg="#E0E0E0",font=("Arial",7))
                message_label11.place(x=520, y=320)
                message_label11.after(1000, lambda: message_label11.destroy())

        try:
                # Check if input value only contains alphabets using regex
            if not re.match("^[0-9]+$", usi13):
                    raise ValueError
            else:
                count = count +1
        except ValueError:
                # If input is invalid, display error message and destroy after 1 sec
                message_label13 = Label(top1, text="Input is invalid!", fg="#FF3333",bg="#E0E0E0",font=("Arial",7))
                message_label13.place(x=320, y=360)
                message_label13.after(1000, lambda: message_label13.destroy())
        try:
                # Check if input value only contains alphabets using regex
            if not re.match("^[0-9]+$", usi14):
                    raise ValueError
            else:
                count = count +1
        except ValueError:
                # If input is invalid, display error message and destroy after 1 sec
                message_label14 = Label(top1, text="Input is invalid!", fg="#FF3333",bg="#E0E0E0",font=("Arial",7))
                message_label14.place(x=520, y=360)
                message_label14.after(1000, lambda: message_label14.destroy())

        try:
                # Check if input value only contains alphabets using regex
            if not re.match("^[0-9]+$", usi16):
                    raise ValueError
            else:
                count = count +1
        except ValueError:
                # If input is invalid, display error message and destroy after 1 sec
                message_label16 = Label(top1, text="Input is invalid!", fg="#FF3333",bg="#E0E0E0",font=("Arial",7))
                message_label16.place(x=320, y=400)
                message_label16.after(1000, lambda: message_label16.destroy())

        try:
                # Check if input value only contains alphabets using regex
            if not re.match("^[0-9]+$", usi17):
                    raise ValueError
            else:
                count = count +1
        except ValueError:
                # If input is invalid, display error message and destroy after 1 sec
                message_label17 = Label(top1, text="Input is invalid!", fg="#FF3333",bg="#E0E0E0",font=("Arial",7))
                message_label17.place(x=520, y=400)
                message_label17.after(1000, lambda: message_label17.destroy())

    def calculate():
        total = 0
        global flag
        try:
            check()
            product = float(e4.get()) * float(e5.get())
            e19.delete(0, END)
            e19.insert(0, "{:.2f}".format(product))
        except ValueError:
            pass

        try:
            check()
            product = float(e7.get()) * float(e8.get())
            e20.delete(0, END)
            e20.insert(0, "{:.2f}".format(product))
        except ValueError:
            pass

        try:
            check()
            product = float(e10.get()) * float(e11.get())
            e21.delete(0, END)
            e21.insert(0, "{:.2f}".format(product))
        except ValueError:
            pass

        try:
            check()
            product = float(e13.get()) * float(e14.get())
            e22.delete(0, END)
            e22.insert(0, "{:.2f}".format(product))
        except ValueError:
            pass

        try:
            check()
            product = float(e16.get()) * float(e17.get())
            e23.delete(0, END)
            e23.insert(0, "{:.2f}".format(product))
        except ValueError:
            pass

        try:
            check()
            total = float(e19.get()) + float(e20.get())+ float(e21.get())+ float(e22.get())+ float(e23.get())
            e18.delete(0, END)
            e18.insert(0, "{:.2f}".format(total))
            flag = True
        except ValueError:
            pass

    def save():
        global flag
        count1 = 5
        count2 = 0
        #for 1st row
        try:
            if ((e3.get() == '-') and (e4.get() == '0') and (e5.get() == '0')):
                medicine_name1 = "NaN"
                medicine_quantity1 = "NaN"
                medicine_price1 = "NaN"

            elif((e3.get() != '-') and (e4.get() != '0') and (e5.get() != '0')):
                medicine_name1 = e3.get()
                medicine_quantity1 = e4.get()
                medicine_price1 = e5.get()
                count2 = count2+1
            else:
                error_label1 = Label(top1, text="Invalid data in row1", fg="#FF3333",bg="#E0E0E0",font=("Arial",10))
                error_label1.place(x=20, y=420)
                error_label1.after(1000, lambda: error_label1.destroy())
                count1 = count1-1
        except ValueError:
            pass

        # for 2nd row
        try:
            if ((e6.get() == '-') and (e7.get() == '0') and (e8.get() == '0')):
                medicine_name2 = "NaN"
                medicine_quantity2 = "NaN"
                medicine_price2 = "NaN"
            elif ((e6.get() != '-') and (e7.get() != '0') and (e8.get() != '0')):
                medicine_name2 = e6.get()
                medicine_quantity2 = e7.get()
                medicine_price2 = e8.get()
                count2 = count2 + 1
            else:
                error_label2 = Label(top1, text="Invalid data in row2", fg="#FF3333", bg="#E0E0E0", font=("Arial", 10))
                error_label2.place(x=20, y=450)
                error_label2.after(1000, lambda: error_label2.destroy())
        except ValueError:
            pass

        #for 3rd row
        try:
            if ((e9.get() == '-') and (e10.get() == '0') and (e11.get() == '0')):
                medicine_name3 = "NaN"
                medicine_quantity3 = "NaN"
                medicine_price3 = "NaN"
            elif ((e9.get() != '-') and (e10.get() != '0') and (e11.get() != '0')):
                medicine_name3 = e9.get()
                medicine_quantity3 = e10.get()
                medicine_price3 = e11.get()
                count2 = count2 + 1
            else:
                error_label3 = Label(top1, text="Invalid data in row3", fg="#FF3333", bg="#E0E0E0", font=("Arial", 10))
                error_label3.place(x=20, y=480)
                error_label3.after(1000, lambda: error_label3.destroy())
        except ValueError:
            pass

        #for 4th row
        try:
            if ((e12.get() == '-') and (e13.get() == '0') and (e14.get() == '0')):
                medicine_name4 = "NaN"
                medicine_quantity4 = "NaN"
                medicine_price4 = "NaN"
            elif ((e12.get() != '-') and (e13.get() != '0') and (e14.get() != '0')):
                medicine_name4 = e9.get()
                medicine_quantity4 = e10.get()
                medicine_price4 = e11.get()
                count2 = count2 + 1
            else:
                error_label4 = Label(top1, text="Invalid data in row4", fg="#FF3333", bg="#E0E0E0", font=("Arial", 10))
                error_label4.place(x=20, y=510)
                error_label4.after(1000, lambda: error_label4.destroy())
                count1 = count1 - 1
        except ValueError:
            pass


        #for 5th row
        try:
            if ((e15.get() == '-') and (e16.get() == '0') and (e17.get() == '0')):
                medicine_name5 = "NaN"
                medicine_quantity5 = "NaN"
                medicine_price5 = "NaN"
            elif ((e15.get() != '-') and (e16.get() != '0') and (e17.get() != '0')):
                medicine_name5 = e9.get()
                medicine_quantity5 = e10.get()
                medicine_price5 = e11.get()
                count2 = count2 + 1
            else:
                error_label5 = Label(top1, text="Invalid data in row5", fg="#FF3333", bg="#E0E0E0", font=("Arial", 10))
                error_label5.place(x=20, y=540)
                error_label5.after(1000, lambda: error_label5.destroy())
                count1 = count1 - 1
        except ValueError:
            pass

        if ((count1 == 5) and (count2 > 0) and flag and (e1.get()!='-') and (e2.get()!='-')):
            global data
            data = [e1.get(), e2.get()
                    ,medicine_name1,medicine_quantity1,medicine_price1
                    ,medicine_name2,medicine_quantity2,medicine_price2
                    ,medicine_name3,medicine_quantity3,medicine_price3
                    ,medicine_name4,medicine_quantity4,medicine_price4
                    ,medicine_name5,medicine_quantity5,medicine_price5
                    ,e18.get()]
            file = open('sell.csv', 'a', newline='')
            writer = csv.writer(file)
            writer.writerow(data)
            file.close()


            df1 = pd.read_csv("quantity.csv")
            if e3.get() != '-':
                df1.loc[df1['medicine_name'] == e3.get(), 'quantity'] -= int(e4.get())
            if e6.get() != '-':
                df1.loc[df1['medicine_name'] == e6.get(), 'quantity'] -= int(e7.get())
            if e9.get() != '-':
                df1.loc[df1['medicine_name'] == e9.get(), 'quantity'] -= int(e10.get())
            if e12.get() != '-':
                df1.loc[df1['medicine_name'] == e12.get(), 'quantity'] -= int(e13.get())
            if e15.get() != '-':
                df1.loc[df1['medicine_name'] == e15.get(), 'quantity'] -= int(e16.get())
            df1.to_csv('quantity.csv', index=False)

            success_label = Label(top1, text="Data added Successfully", fg="green", bg="#E0E0E0", font=("Arial", 15))
            success_label.place(x=350, y=500)
            success_label.after(1000, lambda: success_label.destroy())

            flag = False



    top1.title('Sell Medicines')
    btn = Button(top1, text='Save', width=10, padx=4, pady=3, fg='black', bg='#CCFFCC', activebackground='green',command=save)
    btn.place(x=170, y=550)
    btn1 = Button(top1, text='Quit', width=10, padx=4, pady=3, fg='black', bg='#FF3333', activebackground='red',
                  command=top1.destroy)
    btn1.place(x=650, y=550)

    btn2 = Button(top1, text='Calculate', width=8, padx=1, pady=0.5, fg='black', bg='#FF99CC', activebackground='green',command=calculate)
    btn2.place(x=560, y=420)

    btn3 = Button(top1, text='Print', width=8, padx=4, pady=3, fg='black', bg='#FF99CC', activebackground='green')
    btn3.place(x=410, y=550)


def buy():
    global bg2
    top2 = Toplevel(root)
    top2.title('Update Medicine stocks')
    top2.geometry('900x600')
    top2.maxsize(900, 600)
    top2.minsize(900, 600)

    bg2 = PhotoImage(file=r"C:\Users\Lenovo\Downloads\buuuy.png")
    ca2 = Canvas(top2, width=600, height=400)
    ca2.pack(fill="both", expand=True)
    ca2.create_image(0, 0, image=bg2, anchor="nw")
    ca2.create_text(470, 50, text="Entry Section", font=('Helvetica', 23, 'bold'))

    label1 = Label(top2, text='Medicine Name', font=('Arial', 12, 'bold'), bg='#404040', fg='white')
    label2 = Label(top2, text='Type', font=('Arial', 12, 'bold'), bg='#404040', fg='white')
    label3 = Label(top2, text='Price', font=('Arial', 12, 'bold'), bg='#404040', fg='white')
    label4 = Label(top2, text='Quantity', font=('Arial', 12, 'bold'), bg='#404040', fg='white')
    label5 = Label(top2, text='Mfg date', font=('Arial', 12, 'bold'), bg='#404040', fg='white')
    label6 = Label(top2, text='Exp date', font=('Arial', 12, 'bold'), bg='#404040', fg='white')
    ler = Label(top2,text="", font=('Arial', 12, 'bold'), bg='#404040', fg='red')

    e1 = Entry(top2, width=25)
    e2 = Entry(top2, width=25)
    e3 = Entry(top2, width=25)
    e4 = Entry(top2, width=25)
    e5 = Entry(top2, width=25)
    e6 = Entry(top2, width=25)

    label1.place(x=120, y=100)
    label2.place(x=120, y=160)
    label3.place(x=120, y=220)
    label4.place(x=120, y=280)
    label5.place(x=120, y=340)
    label6.place(x=120, y=400)
    ler.place(x=320,y=430)

    e1.place(x=310, y=100)
    e2.place(x=310, y=160)
    e3.place(x=310, y=220)
    e4.place(x=310, y=280)
    e5.place(x=310, y=340)
    e6.place(x=310, y=400)

    def check():
        global usi1,usi2,usi3,usi4
        usi1 = e1.get()
        usi2 = e2.get()
        usi3 = e3.get()
        usi4 = e4.get()
        usi5 = e5.get()
        usi6 = e6.get()
        count = 0
        try:
            # Check if input value only contains alphabets using regex
            if not re.match("^[a-zA-Z]+$", usi1):
                raise ValueError
            else:
                count = count +1

        except ValueError:
            # If input is invalid, display error message and destroy after 1 sec
            message_label = Label(top2, text="Input is invalid!", fg="#FF3333",bg="#E0E0E0",font=("Arial",11))
            message_label.place(x=335, y=125)
            message_label.after(1000, lambda: message_label.destroy())


        try:
                # Check if input value only contains alphabets using regex
            if not re.match("^[a-zA-Z]+$", usi2):
                    raise ValueError
            else:
                count = count +1
        except ValueError:
                # If input is invalid, display error message and destroy after 1 sec
                message_label1 = Label(top2, text="Input is invalid!", fg="#FF3333",bg="#E0E0E0",font=("Arial",11))
                message_label1.place(x=335, y=185)
                message_label1.after(1000, lambda: message_label1.destroy())

        try:
                # Check if input value only contains alphabets using regex
            if not re.match("^[0-9]+$", usi3):
                    raise ValueError
            else:
                count = count +1
        except ValueError:
                # If input is invalid, display error message and destroy after 1 sec
                message_label2 = Label(top2, text="Input is invalid!", fg="#FF3333",bg="#E0E0E0",font=("Arial",11))
                message_label2.place(x=335, y=245)
                message_label2.after(1000, lambda: message_label2.destroy())

        try:
                # Check if input value only contains alphabets using regex
            if not re.match("^[0-9]+$", usi4):
                    raise ValueError
            else:
                count = count +1
        except ValueError:
                # If input is invalid, display error message and destroy after 1 sec
                message_label3 = Label(top2, text="Input is invalid!", fg="#FF3333",bg="#E0E0E0",font=("Arial",11))
                message_label3.place(x=335, y=305)
                message_label3.after(1000, lambda: message_label3.destroy())

        try:
            # Check if input value is a valid date in the format of dd/mm/yyyy
            if not datetime.datetime.strptime(usi5, '%d/%m/%Y'):
                raise ValueError
            else:
                count = count +1
        except ValueError:
            # If input is invalid, display error message and destroy after 1 sec
            message_label4 = Label(top2, text="Enter date in dd/mm/yyyy format", fg="red")
            message_label4.place(x=290, y=365)
            message_label4.after(1000, lambda: message_label4.destroy())

        try:
            # Check if input value is a valid date in the format of dd/mm/yyyy
            if not datetime.datetime.strptime(usi6, '%d/%m/%Y'):
                raise ValueError
            else:
                count = count + 1
        except ValueError:
            # If input is invalid, display error message and destroy after 1 sec
            message_label5 = Label(top2, text="Enter date in dd/mm/yyyy format", fg="red")
            message_label5.place(x=290, y=425)
            message_label5.after(1000, lambda: message_label5.destroy())

        if count == 6 :
            save()
            message_label6 = Label(top2, text="Details saved Successfully!!", fg="green",font=(20))
            message_label6.place(x=330, y=460)
            message_label6.after(1000, lambda: message_label6.destroy())

    def save():
        global data
        # print(f'{e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get()}\n')
        data = [e1.get(), e2.get(), e3.get(), e4.get(), e5.get(), e6.get()]
        file = open('buy.csv', 'a',newline='')
        writer = csv.writer(file)
        writer.writerow(data)
        file.close()
        df1 = pd.read_csv("quantity.csv")
        if e1.get() != '':
            df1.loc[df1['medicine_name'] == e1.get(), 'quantity'] += int(e4.get())

        df1.to_csv('quantity.csv', index=False)

    def clear():
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e4.delete(0, END)
        e5.delete(0, END)
        e6.delete(0, END)

    btn = Button(top2, text='Save', width=10, padx=4, pady=3, fg='black', bg='#CCFFCC', activebackground='green',
                 command=check)
    btn.place(x=200, y=500)
    btn2 = Button(top2, text='Quit', fg='black', bg='#CCFFCC', activebackground='red', command=top2.destroy, width=10,
                  padx=4, pady=3)
    btn2.place(x=600, y=500)
    btn3 = Button(top2, text='clear', width=10, padx=4, pady=3, fg='black', bg='#CCFFCC', activebackground='green',
                  command=clear)
    btn3.place(x=400, y=500)

    def update_time():
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        current_date = now.strftime("%d-%m-%Y")
        time_label.config(text=current_time)
        date_label.config(text=current_date)
        top2.after(1000, update_time)

    time_label = Label(top2, font=("Helvetica", 30),bg='#606060',fg='red')
    time_label.place(x=700,y=20)



    date_label = Label(top2, font=("Helvetica", 24),bg='#606060',fg='red')
    date_label.place(x=700,y=90)

    update_time()


def summary(expiring_medicines=None):
    top3 = Toplevel(root)
    top3.title('View Stats')
    top3.geometry('700x400')
    top3.maxsize(700, 400)
    top3.minsize(700, 400)
    btn3 = Button(top3, text='Quit', fg='black', bg='#FF3333', activebackground='red', command=top3.destroy, width=10,
                  padx=4, pady=3)
    btn3.place(x=330, y=370)
    label = Label(top3, text="Stat's Section", font=('serif', 70, 'bold'))
    label.place(x=50,y=20)

    # Load data from CSV file
    data1 = pd.read_csv('buy.csv')

    # Function to check if a medicine is expiring on or before the given date
    def check_expiry(row, date):
        exp_date = pd.to_datetime(row['exp_date'], format='%d/%m/%Y')
        return exp_date <= date

    # Function to get the list of expiring medicines
    def get_expiring_medicines(date):
        expiring_medicines = data1.apply(check_expiry, date=date, axis=1)
        return data1[expiring_medicines]

    # Function to handle button click event
    def check_expiry_date():
        # Check if the entered date is valid
        label_error = Label(top3, fg='red')
        label_error.place(x=30, y=200)
        try:
            expiry_date = pd.to_datetime(entry_date.get(), format='%d/%m/%Y')
        except ValueError:

            label_error.config(text='Please enter a valid date in dd/mm/yyyy format')

            return

        # Get the expiring medicines
        expiring_medicines = get_expiring_medicines(expiry_date)

        # If no medicines are expiring, show a message
        if expiring_medicines.empty:
            label_error.config(text='No medicines are expiring on or before the given date.')
            label_error.after(1000, lambda: label_error.destroy())
            return

        details_window = Toplevel(top3)
        details_window.title('Expiring Medicines Details')
        details_window.geometry("300x300")

        Label1 = Label(details_window,text="Expiring medicines details:")
        Label1.place(x=100,y=5)
        text_result = Text(details_window, height=10, width=50)
        text_result.pack(padx=10, pady=10)

        text_result.insert(END, 'The following medicines are expiring on or before the given date:\n\n')
        text_result.insert(END, f"{'Medicine Name':<20}{'Quantity':<10}{'Expiry Date':<15}\n")
        for index, row in expiring_medicines.iterrows():
            text_result.insert(END, f"{row['medicine_name']:<20}{row['quantity']:<10}{row['exp_date']:<15}\n")

        # Disable the text widget so that the user cannot edit the text
        text_result.config(state='disabled')
        details_window.mainloop()


    # Create entry widget to get the expiry date from the user
    label_date = Label(top3, text='Enter expiry date (dd/mm/yyyy):',font=('Calibri',18))
    label_date.place(x=25,y=130)
    entry_date = Entry(top3, width=20)
    entry_date.place(x=40,y=170)

    # Create button widget to check for expiring medicines
    button_check = Button(top3, text='Check',width=8, command=check_expiry_date)
    button_check.place(x=180,y=165)

    # Create a label to display error messages
    global label_error
    label_error = Label(top3, fg='red')
    label_error.place(x=30,y=180)

    #2nd function
    with open('sell.csv') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]

    name_label = Label(top3, text="Enter the customer name: ",font=('Arial',16))
    name_label.place(x=450,y=130)
    name_entry = Entry(top3,width=25)
    name_entry.place(x=470,y=180)

    def validate_input(input_string):
        if not input_string:
            messagebox.showerror("Error", "Please enter a customer name")
            return False
        for char in input_string:
            if not char.isalpha() and not char.isspace():
                messagebox.showerror("Error", "Please enter a valid customer name")
                return False
        return True

    def display_details():
        # get the customer name from the entry widget
        name = name_entry.get()

        # validate the input
        if not validate_input(name):
            return

        # find the customer in the data
        customer = None
        for row in data:
            if row['customer_name'] == name:
                customer = row
                break

        # if the customer is not found, display an error message
        if not customer:
            messagebox.showerror("Error", "Customer name doesn't exist")
            return

        # create a new window to display customer details
        window = Toplevel(top3)
        window.geometry("300x300")

        # create labels for customer name and email
        name_label = Label(window, text=f"Customer Name: {customer['customer_name']}")
        name_label.pack()

        email_label = Label(window, text=f"Customer Email: {customer['customer_mail']}")
        email_label.pack()

        # create labels for medicines bought
        medicines_label = Label(window, text="Medicines Bought")
        medicines_label.pack()

        for i in range(1, 6):
            medicine_name = customer[f'medicine_name{i}']
            if medicine_name == 'Nan':
                continue
            medicine_quantity = customer[f'medicine_quantity{i}']
            medicine_price = customer[f'medicine_price{i}']
            medicine_label = Label(window,
                                      text=f"{medicine_name}: {medicine_quantity} x {medicine_price} = {float(medicine_quantity) * float(medicine_price)}")
            medicine_label.pack()

        # create label for total price
        total_price_label = Label(window, text=f"Total Price: {customer['Total_price']}")
        total_price_label.pack()

    submit_button = Button(top3, text="Submit", command=display_details)
    submit_button.place(x=640,y=175)

    def show_graph():
        df = pd.read_csv('buy.csv')
        df['exp_date'] = pd.to_datetime(df['exp_date'], format='%d/%m/%Y')
        current_date = pd.Timestamp.now()

        expiring_meds_counts = pd.DataFrame(columns=['month', 'count'])
        for i in range(12):
            month = current_date.month_name()[:3]
            count = \
            df[(df['exp_date'] > current_date) & (df['exp_date'] <= current_date + pd.DateOffset(months=1))].shape[0]
            expiring_meds_counts = pd.concat(
                [expiring_meds_counts, pd.DataFrame({'month': month, 'count': count}, index=[0])])
            current_date += pd.DateOffset(months=1)

        plt.bar(expiring_meds_counts['month'], expiring_meds_counts['count'])
        plt.xlabel('Months')
        plt.ylabel('Count')
        plt.title('Expiring Medicines in Next One Year')
        plt.show()

    Lbl1 = Label(top3, text="Expiring medicines Graph:",font=("Arial",17))
    Lbl1.place(x=20, y=250)
    show_button = Button(top3, text="Show", command=show_graph)
    show_button.place(x=100, y=300)

    #pie chart
    def pie():

        df = pd.read_csv('quantity.csv')

        # Extract the medicine names and corresponding quantities
        medicine_names = df['medicine_name'].tolist()
        quantities = df['quantity'].tolist()

        # Calculate the total quantity
        total_quantity = sum(quantities)

        # Calculate the percentage of each medicine in the inventory
        percentages = [q / total_quantity * 100 for q in quantities]

        # Create the pie chart
        labels = [f"{med_name} ({quantities[i]})" for i, med_name in enumerate(medicine_names)]
        plt.pie(percentages, labels=labels, autopct='%1.1f%%')
        plt.title('Medicine Inventory')
        plt.axis('equal')

        # Show the plot
        plt.show()
    lbl = Label(top3,text='Inventory Graph:',font=('Calibri',17))
    lbl.place(x=450,y=250)
    btn1 = Button(top3,text="Show Graph",command=pie)
    btn1.place(x=490,y=300)

# Create Buttons
button1 = Button(root, text="Sell", width=12, bg='#E5FFCC', fg='black', command=sell)
button2 = Button(root, text="Buy", width=12, bg='#E5FFCC', fg='black', command=buy)
button3 = Button(root, text="Summary", width=12, bg='#E5FFCC', fg='black', command=summary)

# Display Buttons
button1_canvas = c1.create_window(200, 500, window=button1)

button2_canvas = c1.create_window(450, 500, window=button2)

button3_canvas = c1.create_window(700, 500, window=button3)

root.mainloop()
