from tkinter import *
import random
import datetime

operator = ''
tax = 0.4
price_food = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65, 1.2]
price_drink = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58, 1.32]
price_dessert = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74, 2.34]
number_invoices = 0
today = ''


def click_button(num):
    global operator
    operator = operator + num
    view_calculator.delete(0, END)
    view_calculator.insert(END, operator)


def delete():
    global operator
    operator = ''
    view_calculator.delete(0, END)


def result_calculator():
    global operator
    result = str(eval(operator))
    view_calculator.delete(0, END)
    view_calculator.insert(0, result)
    operator = ''


def check_check():
    x = 0
    for c in frame_food:
        if var_food[x].get() == 1:
            frame_food[x].config(state=NORMAL)
            if frame_food[x].get() == '0':
                frame_food[x].delete(0, END)
            frame_food[x].focus()
        else:
            frame_food[x].config(state=DISABLED)
            text_food[x].set('0')
        x += 1
    x = 0
    for c in frame_drink:
        if var_drink[x].get() == 1:
            frame_drink[x].config(state=NORMAL)
            if frame_drink[x].get() == '0':
                frame_drink[x].delete(0, END)
            frame_drink[x].focus()
        else:
            frame_drink[x].config(state=DISABLED)
            text_drink[x].set('0')
        x += 1
    x = 0
    for c in frame_dessert:
        if var_dessert[x].get() == 1:
            frame_dessert[x].config(state=NORMAL)
            if frame_dessert[x].get() == '0':
                frame_dessert[x].delete(0, END)
            frame_dessert[x].focus()
        else:
            frame_dessert[x].config(state=DISABLED)
            text_dessert[x].set('0')
        x += 1


def validate_entry(text):
    return text.isdecimal()


def total():
    sub_total_food = 0.0
    p = 0
    for c in text_food:
        sub_total_food = sub_total_food + (float(c.get()) * price_food[p])
        p += 1

    sub_total_drink = 0.0
    p = 0
    for c in text_drink:
        sub_total_drink = sub_total_drink + (float(c.get()) * price_drink[p])
        p += 1

    sub_total_dessert = 0.0
    p = 0
    for c in text_dessert:
        sub_total_dessert = sub_total_dessert + (float(c.get()) * price_dessert[p])
        p += 1

    sub_total = sub_total_food + sub_total_drink + sub_total_dessert
    total_tax = sub_total * tax

    total = sub_total + total_tax

    var_food_cost.set(f'{round(sub_total_food, 2)} €')
    var_drink_cost.set(f'{round(sub_total_drink, 2)} €')
    var_dessert_cost.set(f'{round(sub_total_dessert, 2)} €')
    var_subtotal.set(f'{round(sub_total, 2)} €')
    var_tax.set(f'{round(total_tax, 2)} €')
    var_total.set(f'{round(total, 2)} €')

def generate_number_invoice():
    global number_invoices
    global today
    number_invoices += 1
    date = datetime.date.today().strftime('%Y%m%d')
    date_today = datetime.date.today().strftime('%Y-%m-%d')
    if date_today != today:
        today = date_today
        number_invoices = 0
    return f'{date}{number_invoices}'


def invoice():
    date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    text_invoice.delete(1.0, END)
    num_invoice = f'N#-{generate_number_invoice()}'
    date_invoice = f'{date}'
    text_invoice.insert(END, f'R: {num_invoice}\t\t        fecha:{date_invoice}\n')
    text_invoice.insert(END, f'*' * 56 + '\n')
    text_invoice.insert(END, 'Items\t\tCant.\tCosto  Items\n')
    text_invoice.insert(END, f'-' * 56 + '\n')

    x = 0
    for food in text_food:
        if food.get() != '0':
            text_invoice.insert(END, f'{food_list[x]}\t\t{food.get()}\t'
                                     f'{round(float(food.get()) * price_food[x], 2)} €\n')
            x += 1

    x = 0
    for drink in text_drink:
        if drink.get() != '0':
            text_invoice.insert(END, f'{drinks_list[x]}\t\t{drink.get()}\t'
                                     f'{round(float(drink.get()) * price_drink[x], 2)} €\n')
            x += 1
    x = 0
    for dessert in text_dessert:
        if dessert.get() != '0':
            text_invoice.insert(END, f'{desserts_list[x]}\t\t{dessert.get()}\t'
                                     f'{round(float(dessert.get()) * price_dessert[x], 2)} €\n')
            x += 1

    text_invoice.insert(END, f'-' * 56 +'\n')
    text_invoice.insert(END, f'Costo: \t\t\t{var_subtotal.get()}\n')
    text_invoice.insert(END, f'Tax: \t\t\t{var_subtotal.get()}\n\n')
    text_invoice.insert(END, f'Total: \t\t\t{var_total.get()}\n')

# Init tkinter
app = Tk()
# size app
app.geometry('1020x630+0+0')
# don´t maximize and allows to set size
app.resizable(False, False)
# window title
app.title('titulo prueba')
# background color
app.config(bg='burlywood')
# top panel
top_panel = Frame(app, bd=1, relief=FLAT)
top_panel.pack(side=TOP)
# label title
label_title = Label(top_panel, text='Sistema facturación', fg='azure4', font=('Dosis', 45), bg='burlywood', width=27)
label_title.grid(row=0, column=0)

# left panel
left_panel = Frame(app, bd=1, relief=FLAT)
left_panel.pack(side=LEFT)
# cost panel
cost_panel = Frame(left_panel, bd=1, relief=FLAT, bg='azure4', padx=100)
cost_panel.pack(side=BOTTOM)
# food panel
food_panel = LabelFrame(left_panel,
                        text='Comida',
                        font=('Dosis', 19, 'bold'),
                        bd=1,
                        relief=FLAT,
                        fg='azure4')
food_panel.pack(side=LEFT)
# drink panel
drink_panel = LabelFrame(left_panel,
                         text='Bebidas',
                         font=('Dosis', 19, 'bold'),
                         bd=1,
                         relief=FLAT,
                         fg='azure4')
drink_panel.pack(side=LEFT)
# desert panel
desert_panel = LabelFrame(left_panel,
                          text='Postres',
                          font=('Dosis', 19, 'bold'),
                          bd=1,
                          relief=FLAT,
                          fg='azure4')
desert_panel.pack(side=LEFT)

# right panel
right_panel = Frame(app, bd=1,
                    relief=FLAT)
right_panel.pack(side=RIGHT)
# calc panel
calc_panel = Frame(right_panel,
                   bd=1,
                   relief=FLAT,
                   bg='burlywood')
calc_panel.pack()
# invoice panel
invoice_panel = Frame(right_panel,
                      bd=1,
                      relief=FLAT,
                      bg='burlywood')
invoice_panel.pack()
# buttons panel
buttons_panel = Frame(right_panel,
                      bd=1,
                      relief=FLAT,
                      bg='burlywood')
buttons_panel.pack()

# products list
food_list = ['pollo', 'cordero', 'ternera', 'sardina', 'salmon', 'mero', 'kebab', 'pizza Margarita', 'chicharron']
drinks_list = ['agua', 'refresco', 'soda', 'jugo', 'cafe', 'te', 'vino1', 'vino2', 'vodka']
desserts_list = ['mouse', 'tartaleta', 'gelatina', 'flan', 'helado1', 'helado2', 'tarta1', 'tarta2', 'piña']

# items foods
var_food = []
frame_food = []
text_food = []
count = 0
for food in food_list:
    # make checkbuttons
    var_food.append('')
    var_food[count] = IntVar()
    food = Checkbutton(food_panel,
                       text=food.title(),
                       font=('Dosis', 19, 'bold'),
                       onvalue=1,
                       offvalue=0,
                       variable=var_food[count],
                       command=check_check)
    food.grid(row=count,
              column=0,
              sticky=W)

    # make foods-buttons
    frame_food.append('')
    text_food.append('')
    text_food[count] = StringVar()
    text_food[count].set('0')
    frame_food[count] = Entry(food_panel,
                              font=('Dosis', 18, 'bold'),
                              bd=1,
                              width=4,
                              state=DISABLED,
                              textvariable=text_food[count])
    frame_food[count].grid(row=count,
                           column=1)
    count += 1

# items drinks
var_drink = []
frame_drink = []
text_drink = []
count = 0
for drink in drinks_list:
    # make checkbuttons
    var_drink.append('')
    var_drink[count] = IntVar()
    drink = Checkbutton(drink_panel,
                        text=drink.title(),
                        font=('Dosis', 19, 'bold'),
                        onvalue=1,
                        offvalue=0,
                        variable=var_drink[count],
                        command=check_check)
    drink.grid(row=count,
               column=0,
               sticky=W)

    # make frame drinks-buttons
    frame_drink.append('')
    text_drink.append('')
    text_drink[count] = StringVar()
    text_drink[count].set('0')
    frame_drink[count] = Entry(drink_panel,
                               font=('Dosis', 18, 'bold'),
                               bd=1,
                               width=4,
                               state=DISABLED,
                               textvariable=text_drink[count])
    frame_drink[count].grid(row=count,
                            column=1)
    count += 1

# items deserts
var_dessert = []
frame_dessert = []
text_dessert = []
count = 0
for dessert in desserts_list:
    # make checkbuttons
    var_dessert.append('')
    var_dessert[count] = IntVar()
    dessert = Checkbutton(desert_panel,
                          text=dessert.title(),
                          font=('Dosis', 19, 'bold'),
                          onvalue=1,
                          offvalue=0,
                          variable=var_dessert[count],
                          command=check_check)
    dessert.grid(row=count,
                 column=0,
                 sticky=W)

    # make frame deserts-buttons
    frame_dessert.append('')
    text_dessert.append('')
    text_dessert[count] = StringVar()
    text_dessert[count].set('0')
    frame_dessert[count] = Entry(desert_panel,
                                 font=('Dosis', 18, 'bold'),
                                 bd=1,
                                 width=4,
                                 state=DISABLED,
                                 textvariable=text_dessert[count])
    frame_dessert[count].grid(row=count,
                              column=1)
    count += 1
# variables
var_food_cost = StringVar()
var_drink_cost = StringVar()
var_dessert_cost = StringVar()
var_subtotal = StringVar()
var_tax = StringVar()
var_total = StringVar()

# Label for cost and entry post
label_food_cost = Label(cost_panel,
                        text='Costo Comida',
                        font=('Dosos', 12, 'bold'),
                        bg='azure4',
                        fg='white')
label_food_cost.grid(row=0,
                     column=0)

text_food_cost = Entry(cost_panel,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_food_cost)
text_food_cost.grid(row=0,
                    column=1,
                    padx=41)

label_drink_cost = Label(cost_panel,
                         text='Costo Bebida',
                         font=('Dosis', 12, 'bold'),
                         bg='azure4',
                         fg='white')
label_drink_cost.grid(row=1,
                      column=0)

text_drink_cost = Entry(cost_panel,
                        font=('Dosis', 12, 'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_drink_cost)
text_drink_cost.grid(row=1,
                     column=1,
                     padx=41)

label_dessert_cost = Label(cost_panel,
                           text='Costo Postre',
                           font=('Dosos', 12, 'bold'),
                           bg='azure4',
                           fg='white')
label_dessert_cost.grid(row=2,
                        column=0)

text_dessert_cost = Entry(cost_panel,
                          font=('Dosis', 12, 'bold'),
                          bd=1,
                          width=10,
                          state='readonly',
                          textvariable=var_dessert_cost)
text_dessert_cost.grid(row=2,
                       column=1)

label_subtotal = Label(cost_panel,
                       text='Subtotal',
                       font=('Dosos', 12, 'bold'),
                       bg='azure4',
                       fg='white')
label_subtotal.grid(row=0,
                    column=2)

text_subtotal = Entry(cost_panel,
                      font=('Dosis', 12, 'bold'),
                      bd=1,
                      width=10,
                      state='readonly',
                      textvariable=var_subtotal)
text_subtotal.grid(row=0,
                   column=3)

label_tax = Label(cost_panel,
                  text='Impuesto',
                  font=('Dosis', 12, 'bold'),
                  bg='azure4',
                  fg='white')
label_tax.grid(row=1,
               column=2)

text_tax = Entry(cost_panel,
                 font=('Dosis', 12, 'bold'),
                 bd=1,
                 width=10,
                 state='readonly',
                 textvariable=var_tax)
text_tax.grid(row=1,
              column=3)

label_total = Label(cost_panel,
                    text='total',
                    font=('Dosis', 12, 'bold'),
                    bg='azure4',
                    fg='white')
label_total.grid(row=2,
                 column=2)

text_total = Entry(cost_panel,
                   font=('Dosis', 12, 'bold'),
                   bd=1,
                   width=10,
                   state='readonly',
                   textvariable=var_total)
text_total.grid(row=2,
                column=3)

# Buttons
buttons = ['Total', 'Recibo', 'Guardar', 'Reset']
created_buttons = []
column = 0

for button in buttons:
    button = Button(buttons_panel,
                    text=button.title(),
                    font=('Dosis', 11, 'bold'),
                    fg='white',
                    bg='azure4',
                    bd=1,
                    width=9)
    created_buttons.append(button)
    button.grid(row=0,
                column=column)
    column += 1
created_buttons[0].config(command=total)
created_buttons[1].config(command=invoice)


# invoice
text_invoice = Text(invoice_panel,
                    font=('Dosis', 11, 'bold'),
                    bd=1,
                    width=42,
                    height=10)
text_invoice.grid(row=0,
                  column=0)

# calculator
view_calculator = Entry(calc_panel,
                        font=('Dosis', 11, 'bold'),
                        width=42,
                        bd=1, )
view_calculator.grid(row=0,
                     column=0,
                     columnspan=4)

buttons_calculator = ['7', '8', '9', '+', '4', '5', '6', '-', '1', '2', '3', 'x', 'CE', 'Total', '0', '/']
saved_buttons = []
row = 1
column = 0
for button in buttons_calculator:
    button = Button(calc_panel,
                    text=button.title(),
                    font=('Dosis', 13, 'bold'),
                    fg='white',
                    bg='azure4',
                    bd=1,
                    width=8,
                    height=2
                    )
    saved_buttons.append(button)
    button.grid(row=row,
                column=column)
    if column == 3:
        row += 1

    column += 1

    if column == 4:
        column = 0

saved_buttons[0].config(command=lambda: click_button('7'))
saved_buttons[1].config(command=lambda: click_button('8'))
saved_buttons[2].config(command=lambda: click_button('9'))
saved_buttons[3].config(command=lambda: click_button('+'))
saved_buttons[4].config(command=lambda: click_button('4'))
saved_buttons[5].config(command=lambda: click_button('5'))
saved_buttons[6].config(command=lambda: click_button('6'))
saved_buttons[7].config(command=lambda: click_button('-'))
saved_buttons[8].config(command=lambda: click_button('1'))
saved_buttons[9].config(command=lambda: click_button('2'))
saved_buttons[10].config(command=lambda: click_button('3'))
saved_buttons[11].config(command=lambda: click_button('*'))
saved_buttons[12].config(command=lambda: delete())
saved_buttons[13].config(command=lambda: result_calculator())
saved_buttons[14].config(command=lambda: click_button('0'))
saved_buttons[15].config(command=lambda: click_button('/'))

# prevent it from closing the app
app.mainloop()
