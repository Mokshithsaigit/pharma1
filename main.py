from tkinter import *
import csv
import datetime
from PIL import ImageTk, Image
import re

root = Tk()
root.geometry("900x600")
root.maxsize(900, 600)
root.minsize(900, 600)
root.title("True Pharma's")
bg = PhotoImage(file=r"C:\Users\Lenovo\Downloads\main.png")
c1 = Canvas(root, width=900, height=600)
c1.pack(fill="both", expand=False)
c1.create_image(0, 0, image=bg, anchor="nw")
c1.create_text(450, 120, text="!! Ms Pharmacy !!", font=('serif', 70, 'bold'))


def sell():
    global bg1
    top1 = Toplevel(root)
    top1.geometry('900x600')
    top1.maxsize(900, 600)
    top1.minsize(900, 600)

    bg1 = PhotoImage(file=r"C:\Users\Lenovo\Downloads\sell.png")
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
        #if entry.get() == entry.get().split()[0]:
        if entry.get() == entry.get().split()[0] if len(entry.get().split()) > 0 else entry.get():
            entry.delete(0, "end")

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
            if not re.match("^[a-zA-Z-]+$", usi1):
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
            if not re.match("^[a-zA-Z-]+$", usi2):
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
        sum = 0
        for entry in [e5, e8, e11, e14, e17]:
                try:
                    value = int(entry.get())
                    sum += value
                except ValueError:

                # If the entry section doesn't contain a valid integer, skip it
                    pass
        e18.delete(0, END)
        e18.insert(0, sum)

    top1.title('Sell Medicines')
    btn = Button(top1, text='Save', width=10, padx=4, pady=3, fg='black', bg='#CCFFCC', activebackground='green',command=check)
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


def summary():
    top3 = Toplevel(root)
    top3.title('View Stats')
    top3.geometry('600x400')
    top3.maxsize(600, 400)
    top3.minsize(600, 400)
    btn3 = Button(top3, text='Quit', fg='black', bg='#FF3333', activebackground='red', command=top3.destroy, width=10,
                  padx=4, pady=3)
    btn3.place(x=270, y=350)


# Create Buttons
button1 = Button(root, text="Sell", width=12, bg='#E5FFCC', fg='black', command=sell)
button2 = Button(root, text="Buy", width=12, bg='#E5FFCC', fg='black', command=buy)
button3 = Button(root, text="Summary", width=12, bg='#E5FFCC', fg='black', command=summary)

# Display Buttons
button1_canvas = c1.create_window(200, 500, window=button1)

button2_canvas = c1.create_window(450, 500, window=button2)

button3_canvas = c1.create_window(700, 500, window=button3)

root.mainloop()
