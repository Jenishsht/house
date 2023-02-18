from tkinter import *
from tkinter import ttk
import banglore_home_prices_final as data
import tkinter.messagebox as Messagebox

def estimate():
    if int(bhk.get())+2 < int(bath.get()):
        Messagebox.showwarning('Error','Bathrooms cannot be 2 more than BHK')
    elif not(area.get().isdigit()):
        Messagebox.showwarning('Error', 'Area value invalid')
    elif int(area.get()) < 300:
        Messagebox.showwarning('Error', 'Area cannot be less than 300')
    else:
        output=data.predict_price(loc.get(),area.get(),bhk.get(),bath.get())
        Messagebox.showinfo('Price(Lakhs)',round(output,2))

root = Tk()
root.geometry('500x500')

l1 = Label(root, text="Area (Square Feet)")
l1.place(x=20, y=20)

area = Entry(root)
area.place(x=200, y=20)

bhk_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

l2 = Label(root, text="BHK")
l2.place(x=20, y=80)

bhk = ttk.Combobox(root, values=bhk_list)
bhk.place(x=200, y=80)

bathrooms = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

l3 = Label(root, text="Bathroom")
l3.place(x=20, y=140)

bath = ttk.Combobox(root, values=bathrooms)
bath.place(x=200, y=140)

locations = list(data.List)

l4 = Label(root, text="Location")
l4.place(x=20, y=200)

loc = ttk.Combobox(root, values=locations)
loc.place(x=200, y=200)

btn = Button(root, text="Estimate price", command=lambda: estimate())
btn.place(x=80, y=260)

root.mainloop()
