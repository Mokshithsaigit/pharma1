import pandas as pd
import matplotlib.pyplot as plt
from tkinter import *


def show_graph():
    df = pd.read_csv('buy.csv')
    df['exp_date'] = pd.to_datetime(df['exp_date'], format='%d/%m/%Y')
    current_date = pd.Timestamp.now()

    expiring_meds_counts = pd.DataFrame(columns=['month', 'count'])
    for i in range(12):
        month = current_date.month_name()[:3]
        count = df[(df['exp_date'] > current_date) & (df['exp_date'] <= current_date + pd.DateOffset(months=1))].shape[0]
        expiring_meds_counts = pd.concat([expiring_meds_counts, pd.DataFrame({'month': month, 'count': count}, index=[0])])
        current_date += pd.DateOffset(months=1)

    plt.bar(expiring_meds_counts['month'], expiring_meds_counts['count'])
    plt.xlabel('Months')
    plt.ylabel('Count')
    plt.title('Expiring Medicines in Next One Year')
    plt.show()


root = Tk()
root.geometry("200x100")

show_button = Button(root, text="Show", command=show_graph)
show_button.pack()

root.mainloop()
