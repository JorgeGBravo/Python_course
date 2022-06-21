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
label_title = Label(top_panel, text='Sistema facturacion', fg='azure4', font=('Dosis', 45), bg='burlywood', width=27)
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

# products list
food_list = ['pollo', 'cordero', 'ternera', 'sardina', 'salmon', 'mero', 'kebab', 'pizza Margarita', 'chicharron' ]
drinks_list = ['agua', 'refresco', 'soda', 'jugo', 'cafe', 'te', 'vino1','vino2', 'vodka']
deserts_list = ['mouse', 'tartaleta', 'gelatina', 'flan', 'helado1', 'helado2', 'tarta1', 'tarta2', 'piña']

# checkbuttons
# itams foods
var_food= []
count = 0
for food in food_list:
    var_food.append('')
    var_food[count] = IntVar()
    food = Checkbutton(food_panel, text=food.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable=var_food[count])
    food.grid(row=count, column=0, sticky=W)
    count += 1

# itams foods
var_drink = []
count = 0
for drink in drinks_list:
    var_drink.append('')
    var_drink[count] = IntVar()
    drink = Checkbutton(drink_panel, text=drink.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable=var_drink[count])
    drink.grid(row=count, column=0, sticky=W)
    count += 1

# itams foods
var_desert = []
count = 0
for desert in deserts_list:
    var_desert.append('')
    var_desert[count] = IntVar()
    desert= Checkbutton(desert_panel, text=desert.title(), font=('Dosis', 19, 'bold'), onvalue=1, offvalue=0, variable=var_desert[count])
    desert.grid(row=count, column=0, sticky=W)
    count += 1

# prevent it from closing the app
app.mainloop()

