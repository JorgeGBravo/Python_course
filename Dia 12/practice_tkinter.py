from tkinter import *

# Init tkinter
app = Tk()
# size app
app.geometry('1020x630+0+0')
# don´t maximize and allows to set size
app.resizable(0, 0)
# window title
app.title('titulo prueba')
# background color
app.config(bg='burlywood')
# top panel
top_panel = Frame(app, bd=1, relief=FLAT)
top_panel.pack(side=TOP)
# label title
label_title = Label(top_panel, text='Sistema facturacion', fg='azure4', font=('Dosis', 58), bg='burlywood', width=27)
label_title.grid(row=0, column=0)

# left panel
left_panel = Frame(app, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)
# cost panel
cost_panel = Frame(left_panel, bd=1, relief=FLAT)
cost_panel.pack(side=BOTTOM)
# food panel
food_panel = LabelFrame(left_panel, text='Comida', font=('Dosis', 19, 'bold'),bd=1, relief=FLAT, fg='azure4')
food_panel.pack(side=LEFT)
# drink panel
drink_panel = LabelFrame(left_panel, text='Bebidas', font=('Dosis', 19, 'bold'),bd=1, relief=FLAT, fg='azure4')
drink_panel.pack(side=LEFT)
# desert panel
desert_panel = LabelFrame(left_panel, text='Postres', font=('Dosis', 19, 'bold'),bd=1, relief=FLAT, fg='azure4')
desert_panel.pack(side=LEFT)

# right panel
right_panel = Frame(app, bd=1, relief=FLAT)
right_panel.pack(side=RIGHT)
# calc panel
calc_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood')
calc_panel.pack()
# invoice panel
invoice_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood')
invoice_panel.pack()
# buttons panel
buttons_panel = Frame(right_panel, bd=1, relief=FLAT, bg='burlywood')
buttons_panel.pack()

# prevent it from closing the app
app.mainloop()

