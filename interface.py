from tkinter import *
from tkinter import Tk
from tkinter import StringVar
from tkinter import ttk
from tkinter import messagebox
from PIL import Image
from PIL import ImageTk
from tkcalendar import DateEntry
from manipulationDB import *

""" COLORS """

co0 = "#2e2d2b"  # Black
co1 = "#feffff"  # White
co2 = "#4fa882"  # green
co3 = "#38576b"  # value
co4 = "#403d3d"   # letter
co5 = "#e06636"   # - profit
co6 = "#038cfc"   # blue
co7 = "#3fbfb9"   # green
co8 = "#263238"   # + green
co9 = "#e9edf5"   # + green


""" Creating Window """

window = Tk ()
window.title ("")
window.geometry('900x600')
window.configure(background=co9)
window.resizable(width=FALSE, height=FALSE)

style = ttk.Style(window)
style.theme_use("clam")



""" FRAMES """ 

frameUp = Frame(window, width=1043, height=50, bg=co1,  relief=FLAT)
frameUp.grid(row=0, column=0)

frameMiddle = Frame(window,width=1043, height=303,bg=co1, pady=20, relief=FLAT)
frameMiddle.grid(row=1, column=0,pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(window,width=1043, height=300,bg=co1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)

""" FUNCTIONS """

# Function insert
def insert():

    # Get the values of the input fields
    name = e_name.get()
    location = e_location.get()
    description = e_description.get()
    brand = e_brand.get()
    date_of_purchase = e_date_of_purchase.get()
    purchase_value = e_value.get()

    # List of data to be entered
    list_insert = [name, location, description, brand, date_of_purchase, purchase_value]

    # Check that all fields have been filled in
    for idx in list_insert:
        if idx == "":
            messagebox.showerror("Error", "Enter all the necessary fields. ")
            return
    
    # Call function to insert data into the database
    insert_form(list_insert)
    messagebox.showinfo("Sucess","Data entered. ")

    # Clear input fields after insertion
    e_name.delete(0, "end")
    e_location.delete(0, "end")
    e_description.delete(0, "end")
    e_brand.delete(0, "end")
    e_date_of_purchase.delete(0, "end")
    e_value.delete(0, "end")

    # Update the view of the inserted items table
    tables()

# Function update
def att():
    try:
        # Get the data of the selected row in the treeview
        treev_datas = tree.focus() # Get the focused item in the treeview
        treev_dictionary = tree.item(treev_datas)  # Get a dictionary with the item values
        treev_list = treev_dictionary['values'] # Get a list of the values of the selected item

        # Extract the ID of the first value in the list
        value = treev_list[0]

        # Clear input fields
        e_name.delete(0, "end")
        e_location.delete(0, "end")
        e_description.delete(0, "end")
        e_brand.delete(0, "end")
        e_date_of_purchase.delete(0, "end")
        e_value.delete(0, "end")

        id = int(value)

        # Fill in the input fields with the data of the selected item
        e_name.insert(0, treev_list[1])
        e_location.insert(0, treev_list[2])
        e_description.insert(0, treev_list[3])
        e_brand.insert(0, treev_list[4])
        e_date_of_purchase.insert(0, treev_list[5])
        e_value.insert(0, treev_list[6])

        def update():
            # Get the updated values of the input fields
            name = e_name.get()
            location = e_location.get()
            description = e_description.get()
            brand = e_brand.get()
            date_of_purchase = e_date_of_purchase.get()
            purchase_value = e_value.get()

            # List of data to be updated, including ID
            list_att = [name, location, description, brand, date_of_purchase, purchase_value, id]

            for idx in list_att:
                if idx == "":
                    messagebox.showerror("Error", "Enter all the necessary fields. ")
                    return
            
            # Call function to update data in the database
            update_form(list_att)
            messagebox.showinfo("Sucess","Updated data. ")

            # Clear input fields after update
            e_name.delete(0, "end")
            e_location.delete(0, "end")
            e_description.delete(0, "end")
            e_brand.delete(0, "end")
            e_date_of_purchase.delete(0, "end")
            e_value.delete(0, "end")

            # Remove the confirmation button after the update
            button_confirm.destroy()

            tables()

         # Create confirmation button to start the update process
        button_confirm = Button(frameMiddle,command=update, text="confirm".upper(), width=13, overrelief=RIDGE,  font=('ivy 8 bold'),bg=co2, fg=co1)
        button_confirm.place(x=330, y=185)
    except IndexError:
        messagebox.showerror("Error", "Select data from the table")

# Function delete
def delete():
    try:
        # Get the data of the selected row in the treeview
        treev_datas = tree.focus() # Get the focused item in the treeview
        treev_dictionary = tree.item(treev_datas)  # Get a dictionary with the item values
        treev_list = treev_dictionary['values'] # Get a list of the values of the selected item

        # Extract the ID of the first value in the list
        value = treev_list[0]

        # Call function to delete data in the database
        delete_form([value])
        
        messagebox.showinfo("Sucess","Deleted data. ")

        tables()

    except IndexError:
        messagebox.showerror("Error", "Select data from the table")

def search():
    try:
        id_search = e_search.get()

        item = view_item(id_search)
        
        if item:
            messagebox.showinfo("Success", f"Item found: {item}")
        else:
            messagebox.showinfo("Information", "Item not found.")
        tables()
    except IndexError:
        messagebox.showerror("Error", "Select data from the table")


""" OPEN IMAGE """
app_img  = Image.open('/inventory/images/Inventory.png')
app_img = app_img.resize((45, 45))
app_img = ImageTk.PhotoImage(app_img)

app_logo = Label(frameUp, image=app_img, text="Inventory", width=900, compound=LEFT, relief=RAISED, anchor=NW, font=('Verdana 20 bold'),bg=co1, fg=co4 )
app_logo.place(x=0, y=0)

""" CREATING ENTRIES """
l_name = Label(frameMiddle, text="Name", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_name.place(x=10, y=10)

e_name = Entry(frameMiddle, width=30, justify='left',relief="solid")
e_name.place(x=130, y=11)


l_location = Label(frameMiddle, text="Location", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_location.place(x=10, y=40)

e_location = Entry(frameMiddle, width=30, justify='left',relief="solid")
e_location.place(x=130, y=41)

l_description = Label(frameMiddle, text="Description", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_description.place(x=10, y=70)

e_description = Entry(frameMiddle, width=30, justify='left',relief="solid")
e_description.place(x=130, y=71)

l_brand = Label(frameMiddle, text="Brand", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_brand.place(x=10, y=100)

e_brand = Entry(frameMiddle, width=30, justify='left',relief="solid")
e_brand.place(x=130, y=101)

l_date_of_purchase = Label(frameMiddle, text="Date of purchase", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_date_of_purchase.place(x=10, y=130)
 
e_date_of_purchase = DateEntry(frameMiddle, width=12, background='darkblue', foreground='white', borderwidth=2, year=2020)
e_date_of_purchase.place(x=130, y=131)

l_value = Label(frameMiddle, text="Purchase value", height=1,anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4)
l_value.place(x=10, y=160)

e_value = Entry(frameMiddle, width=30, justify='left',relief="solid")
e_value.place(x=130, y=161)


e_search = Entry(frameUp, width=30, justify='left',relief="solid")
e_search.place(x=600, y=25)


""" BUTTONS TAHT WILL PERFORM THE CRUD FUNCTIONS """
# Button INSERT
img_add  = Image.open('/inventory/images/add.png')
img_add = img_add.resize((20, 20))
img_add = ImageTk.PhotoImage(img_add)

button_insert = Button(frameMiddle,command=insert,image=img_add, compound=LEFT, anchor=NW, text="add".upper(), width=95, overrelief=RIDGE,  font=('ivy 8'),bg=co1, fg=co0)
button_insert.place(x=330, y=10)

# Button Update
img_update  = Image.open('/inventory/images/update.png')
img_update = img_update.resize((20, 20))
img_update = ImageTk.PhotoImage(img_update)

button_update = Button(frameMiddle,command=att, image=img_update, compound=LEFT, anchor=NW, text="update".upper(), width=95, overrelief=RIDGE,  font=('ivy 8'),bg=co1, fg=co0)
button_update.place(x=330, y=50)


# Button Delete
img_delete  = Image.open('/inventory/images/delete.png')
img_delete = img_delete.resize((20, 20))
img_delete = ImageTk.PhotoImage(img_delete)
button_delete = Button(frameMiddle,command=delete, image=img_delete, compound=LEFT, anchor=NW, text="Delete".upper(), width=95, overrelief=RIDGE,  font=('ivy 8'),bg=co1, fg=co0)
button_delete.place(x=330, y=90)


# Button view item
img_search = Image.open('/inventory/images/search.png')
img_search = img_search.resize((20,20))
img_search = ImageTk.PhotoImage(img_search)
button_search = Button(frameUp,command=search,image=img_search, compound=LEFT, anchor=NW, text="Search".upper(), width=95, overrelief=RIDGE,  font=('ivy 8'),bg=co1, fg=co0)
button_search.place(x=795, y=20)

# Labels Quantidade total e Valores
l_total = Label(frameMiddle, width=14, height=2,anchor=CENTER, font=('Ivy 17 bold'), bg=co7, fg=co1)
l_total.place(x=450, y=19)

l_value_total = Label(frameMiddle, text='Total value' ,anchor=NW, font=('Ivy 9 bold'), bg=co7, fg=co1)
l_value_total.place(x=450, y=19)


l_qtd = Label(frameMiddle, width=10, height=2,anchor=CENTER, font=('Ivy 25 bold'), bg=co7, fg=co1)
l_qtd.place(x=450, y=92)

l_qtd_itens = Label(frameMiddle, text='Quantity of items' ,anchor=NW, font=('Ivy 9 bold'), bg=co7, fg=co1)
l_qtd_itens.place(x=460, y=94)


# Function to show information about inventory
def tables():

    global tree
    # creating a treeview with dual scrollbars
    tabela_head = ['#Item','Name', 'Location','Description', 'Brand', 'Date of purchase','Purchase value']

    list_items = view_inventory()

    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    # horizontal scrollbar
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)


    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center"]
    h=[100,150,150,150,130,100,100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)

        # adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])

        n+=1

    for item in list_items:
        tree.insert('', 'end', values=item)


    quantity = []

    for iten in list_items:
        quantity.append(iten[6])


    total_value = sum(quantity)
    total_items = len(quantity)

    l_total['text'] = 'R$ {:,.2f}'.format(total_value)
    l_qtd['text'] = total_items