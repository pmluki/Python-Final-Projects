from tkinter import *
from tkinter import messagebox
from tkinter import ttk


class GUI:
    def __init__(self, window):
        '''
        CHECKBOX CHECKED: Check later to see if the check boxes are selected.
        LABEL TITLE: Tkinter Label that says the name of the restaurant.
        LABEL MENU TITLE: Tkinter Label that guides the user and lets them know that entrees come with 2 sides.
        APP LABEL: Tkinter Label that lets the user know this section contains appitizers.
        ENTREE LABEL: Tkinter Label that lets the user know this section contains entrees.
        SIDES LABEL: Tkinter Label that lets the user know this section contains sides.
        DRINK LABEL: Tkinter Label that lets the user know this section contains drinks.
        DESSERT LABEL: Tkinter Label that lets the user know this section contains desserts.
        :param window: Window is the (GUI) application when it runs.
        '''

        # SECTION COMPLETE

        self.window = window

        self.label_title = Label(self.window, text='Paige\'s Restaurant', font=('Ariel', 30))
        self.label_title.pack()

        self.label_menu_title = Label(text='Select what you would like to order, and submit it to be completed when ready!', font=('Ariel', 12))
        self.label_menu_title.pack(side='top')

        self.app_label = Label(self.window, text='Appetizers', font=('Ariel', 15))
        self.app_label.place(x=75, y=100)

        self.entree_label = Label(self.window, text='Entrees', font=('Ariel', 15))
        self.entree_label.place(x=245, y=100)

        self.sides_label = Label(self.window, text='Sides', font=('Ariel', 15))
        self.sides_label.place(x=380, y=100)

        self.drink_label = Label(self.window, text='Drinks', font=('Ariel', 15))
        self.drink_label.place(x=505, y=100)

        self.dessert_label = Label(self.window, text='Desserts', font=('Ariel', 15))
        self.dessert_label.place(x=625, y=100)

        # ------------------------------------------------
        # --- BELOW HERE IS CUSTOMER INFORMATION INPUT ---
        # ------------------------------------------------

        '''SECTION COMPLETE'''

        self.cust_strVar = StringVar()

        self.cust_name_label = Label(self.window, text='Input Name For Order:', font=('Ariel', 12))
        self.cust_name_label.place(x=45, y=375)

        self.cust_name_entry = Entry(self.window, textvariable=self.cust_strVar)
        self.cust_name_entry.place(x=210, y=378)

        # -------------------------------------------
        # --- BELOW HERE IS TIP INFORMATION INPUT ---
        # -------------------------------------------
        '''
        SELECTION: Allows for the default selection to be chosen and only one button to be selected
        TIP LABEL: Lets the user know that this is for tipping
        RBUTTON NONE: Leaves no tip --SET AS DEFAULT WITH SELECTION.SET(1)--
        RBUTTON 10: Leaves 10% tip
        RBUTTON 15:Leaves 15% tip
        RBUTTON 20: Leaves 20% tip
        '''

        ''''SECTION COMPLETE'''
        self.selection = IntVar()

        self.tip_label = Label(self.window, text='Tip:', font=('Ariel', 12)).place(x=450, y=375)
        self.selection.set(1)
        self.rbutton_none = Radiobutton(self.window, text='None', variable=self.selection, value=1)
        self.rbutton_none.place(x=500, y=375)

        self.rbutton_10 = Radiobutton(self.window, text='10%', variable=self.selection, value=2)
        self.rbutton_10.place(x=565, y=375)

        self.rbutton_15 = Radiobutton(self.window, text='15%', variable=self.selection, value=3)
        self.rbutton_15.place(x=625, y=375)

        self.rbutton_20 = Radiobutton(self.window, text='20%', variable=self.selection, value=4)
        self.rbutton_20.place(x=680, y=375)

        # ----------------------------------
        # --- BELOW HERE IS CLEAR BUTTON ---
        # ----------------------------------

        self.clear_button = Button(self.window, text='Reset', font=('Ariel', 12), width=10, height=2, command=self.clear)
        self.clear_button .place(x=350, y=525)

        # -----------------------------------
        # --- BELOW HERE IS SUBMIT BUTTON ---
        # -----------------------------------

        self.submit_button = Button(self.window, text='Submit', font=('Ariel', 12), width=10, height=2, command=self.submit)
        self.submit_button.place(x=50, y=525)

        # ----------------------------
        # --- CHANGING LABELS HERE ---
        # ----------------------------

        self.order_sum = Label(self.window, text='', font=('Ariel', 12))
        self.order_sum.place(x=50, y=420)

        self.sum_name = Label(self.window, text='', font=('Ariel', 12))
        self.sum_name.place(x=52, y=450)

        self.sum_total = Label(self.window, text='', font=('Ariel', 12, 'underline'))
        self.sum_total.place(x=284, y=450)

        self.sum_food = Label(self.window, text='', font=('Ariel', 12, 'underline'))
        self.sum_food.place(x=505, y=420)

        self.sum_tax = Label(self.window, text='', font=('Ariel', 12, 'underline'))
        self.sum_tax.place(x=515, y=450)

        self.sum_tip = Label(self.window, text='', font=('Ariel', 12, 'underline'))
        self.sum_tip.place(x=517, y=480)

        self.sum_name_input = Label(self.window, text='', font=('Ariel', 12))
        self.sum_name_input.place(x=175, y=450)

        self.sum_total_input = Label(self.window, text='', font=('Ariel', 12))
        self.sum_total_input.place(x=332, y=451)

        self.sum_food_input = Label(self.window, text='', font=('Ariel', 12))
        self.sum_food_input.place(x=552, y=421)

        self.sum_tax_input = Label(self.window, text='', font=('Ariel', 12))
        self.sum_tax_input.place(x=552, y=451)

        self.sum_tip_input = Label(self.window, text=f'', font=('Ariel', 12))
        self.sum_tip_input.place(x=552, y=481)

        # ------------------------
        # --- IF BILL IS SPLIT ---
        # ------------------------

        '''
        If the bill is not split, the changing labels above will show
        These labels will only appear if the bill is split between 2, 3, or 4 people.
        '''
        self.bill_split_name = Label(self.window, text='', font=('Ariel', 12))
        self.bill_split_name.place(x=50, y=450)

        self.bill_1 = Label(self.window, text='', font=('Ariel', 12, 'underline'))
        self.bill_1.place(x=250, y=420)

        self.bill_2 = Label(self.window, text='', font=('Ariel', 12, 'underline'))
        self.bill_2.place(x=375, y=420)

        self.bill_3 = Label(self.window, text='', font=('Ariel', 12, 'underline'))
        self.bill_3.place(x=500, y=420)

        self.bill_4 = Label(self.window, text='', font=('Ariel', 12, 'underline'))
        self.bill_4.place(x=650, y=420)

        # -- Bill 1 information --

        self.bill_1_food_total = 0
        self.bill_1_tax_total = 0
        self.bill_1_tip_total = 0
        self.bill_1_total = 0

        self.bill_1_food = Label(self.window, text='', font=('Ariel', 10))
        self.bill_1_food.place(x=250, y=445)

        self.bill_1_tax = Label(self.window, text='', font=('Ariel', 10))
        self.bill_1_tax.place(x=250, y=463)

        self.bill_1_tip = Label(self.window, text='', font=('Ariel', 10))
        self.bill_1_tip.place(x=250, y=481)

        self.bill_1_total_label = Label(self.window, text='', font=('Ariel', 10))
        self.bill_1_total_label.place(x=250, y=499)

        # Bill 2

        self.bill_2_food = Label(self.window, text='', font=('Ariel', 10))
        self.bill_2_food.place(x=375, y=445)

        self.bill_2_tax = Label(self.window, text='', font=('Ariel', 10))
        self.bill_2_tax.place(x=375, y=463)

        self.bill_2_tip = Label(self.window, text='', font=('Ariel', 10))
        self.bill_2_tip.place(x=375, y=481)

        self.bill_2_total_label = Label(self.window, text='', font=('Ariel', 10))
        self.bill_2_total_label.place(x=375, y=499)

        # Bill 3

        self.bill_3_food = Label(self.window, text='', font=('Ariel', 10))
        self.bill_3_food.place(x=500, y=445)

        self.bill_3_tax = Label(self.window, text='', font=('Ariel', 10))
        self.bill_3_tax.place(x=500, y=463)

        self.bill_3_tip = Label(self.window, text='', font=('Ariel', 10))
        self.bill_3_tip.place(x=500, y=481)

        self.bill_3_total_label = Label(self.window, text='', font=('Ariel', 10))
        self.bill_3_total_label.place(x=500, y=499)

        # Bill 4

        self.bill_4_food = Label(self.window, text='', font=('Ariel', 10))
        self.bill_4_food.place(x=650, y=445)

        self.bill_4_tax = Label(self.window, text='', font=('Ariel', 10))
        self.bill_4_tax.place(x=650, y=463)

        self.bill_4_tip = Label(self.window, text='', font=('Ariel', 10))
        self.bill_4_tip.place(x=650, y=481)

        self.bill_4_total_label = Label(self.window, text='', font=('Ariel', 10))
        self.bill_4_total_label.place(x=650, y=499)

        # --------------------------
        # --- SPLITTING THE BILL ---
        # --------------------------

        self.split_bill = Label(self.window, text="Split the bill:", font=('Ariel', 12))
        self.split_bill.place(x=394, y=350)
        self.bill_split = IntVar()
        self.bill_split.set(5)

        self.split_bill_no = Radiobutton(self.window, text='No', variable=self.bill_split, value=5)
        self.split_bill_no.place(x=500, y=350)

        self.split_bill_2 = Radiobutton(self.window, text='2', variable=self.bill_split, value=6)
        self.split_bill_2.place(x=565, y=350)

        self.split_bill_3 = Radiobutton(self.window, text='3', variable=self.bill_split, value=7)
        self.split_bill_3.place(x=625, y=350)

        self.split_bill_4 = Radiobutton(self.window, text='4', variable=self.bill_split, value=8)
        self.split_bill_4.place(x=680, y=350)


        # ---------------------------------
        # --- BELOW HERE IS EXIT SET UP ---
        # ---------------------------------

        self.exit_button = Button(self.window, text='Exit', font=('Ariel', 12), width=10, height=2, command=window.destroy)
        self.exit_button.place(x=625, y=525)

        #----------------------------------
        # --- BELOW HERE IS MENU SET UP ---
        #----------------------------------

        '''
        APPETIZERS
        ----------
        A1: Checkbutton and Label for jalapeno popper appetizer. Label provides a description, check box lets it be selected.
        A2: Checkbutton and Label for fried pickles. Label provides a description, check box lets it be selected.
        A3: Checkbutton and Label for pulled pork nachos. Label provides a description, check box lets it be selected.
        '''

        self.button_a1 = IntVar()
        self.button_a2 = IntVar()
        self.button_a3 = IntVar()

        self.cbutton_a1 = Checkbutton(self.window, text='Jalapeno Poppers ($6)', variable=self.button_a1, font=('Ariel', 10))
        self.cbutton_a1.place(x=50, y=125)

        self.a1_label= Label(self.window, text='A breaded and cream cheese         \nstuffed jalapeno deep fried and       \nserved with ranch.                           ', font=('Ariel', 8))
        self.a1_label.place(x=50, y=150)

        self.cbutton_a2 = Checkbutton(self.window, text='Fried Pickles ($5)',  variable=self.button_a2, font=('Ariel', 10))
        self.cbutton_a2.place(x=50, y=200)

        self.a2_label = Label(self.window, text='A breaded pickle chip deep fried\n and served with ranch.                ', font=('Ariel', 8))
        self.a2_label.place(x=47, y=225)

        self.cbutton_a3 = Checkbutton(self.window, text='Pulled Pork Nachos ($8)',  variable=self.button_a3, font=('Ariel', 10))
        self.cbutton_a3.place(x=50, y=265)

        self.a3_label = Label(self.window, text='Nachos served with pulled pork,     \nsour cream, three cheese queso,    \njalapenos, black beans, and             \nguacamole.                                        ',font=('Ariel', 8))
        self.a3_label.place(x=47, y=285)

        '''
        ENTREES
        -------
        E1: Checkbutton and Label for ribeye entree. Label provides a description, check box lets it be selected.
        E2: Checkbutton and Label for filet mignon entree. Label provides a description, check box lets it be selected.
        E3: Checkbutton and Label for petite sirloin entree. Label provides a description, check box lets it be selected.
        E4: Checkbutton and Label for top sirloin entree. Label provides a description, check box lets it be selected.
        E5: Checkbutton and Label for salmon filet entree. Label provides a description, check box lets it be selected.
        '''

        self.button_e1 = IntVar()
        self.button_e2 = IntVar()
        self.button_e3 = IntVar()
        self.button_e4 = IntVar()
        self.button_e5 = IntVar()

        self.cbutton_e1 = Checkbutton(self.window, text='Ribeye ($35)', variable=self.button_e1, font=('Ariel', 10))
        self.cbutton_e1.place(x=225, y=125)

        self.e1_label = Label(self.window, text='16 oz', font=('Ariel', 8))
        self.e1_label.place(x=247, y=145)

        self.cbutton_e2 = Checkbutton(self.window, text='Filet Mignon ($39)', variable=self.button_e2, font=('Ariel', 10))
        self.cbutton_e2.place(x=225, y=165)

        self.e2_label = Label(self.window, text='8 oz', font=('Ariel', 8))
        self.e2_label.place(x=247, y=185)

        self.cbutton_e3 = Checkbutton(self.window, text='Petite Sirloin ($20)', variable=self.button_e3, font=('Ariel', 10))
        self.cbutton_e3.place(x=225, y=205)

        self.e3_label = Label(self.window, text='12 oz', font=('Ariel', 8))
        self.e3_label.place(x=247, y=225)

        self.cbutton_e4 = Checkbutton(self.window, text='Top Sirloin ($30)', variable=self.button_e4, font=('Ariel', 10))
        self.cbutton_e4.place(x=225, y=245)

        self.e4_label = Label(self.window, text='22 oz', font=('Ariel', 8))
        self.e4_label.place(x=247, y=265)

        self.cbutton_e5 = Checkbutton(self.window, text='Salmon Filet ($22)', variable=self.button_e5, font=('Ariel', 10))
        self.cbutton_e5.place(x=225, y=285)

        self.e5_label = Label(self.window, text='Salmon Filet served              \nwith a lemon wedge.            ', font=('Ariel', 8))
        self.e5_label.place(x=247, y=305)

        '''
        SIDES
        -----
        5 sides for the user to choose from
        IntVars lets the program store the price of the item.
        '''

        self.button_s1 = IntVar()
        self.button_s2 = IntVar()
        self.button_s3 = IntVar()
        self.button_s4 = IntVar()
        self.button_s5 = IntVar()

        self.cbutton_s1 = Checkbutton(self.window, text='Broccoli ($2)', variable=self.button_s1, font=('Ariel', 10))
        self.cbutton_s1.place(x=360, y=125)

        self.cbutton_s2 = Checkbutton(self.window, text='Corn ($2)', variable=self.button_s2, font=('Ariel', 10))
        self.cbutton_s2.place(x=360, y=145)

        self.cbutton_s3 = Checkbutton(self.window, text='Asparagus ($3)', variable=self.button_s3, font=('Ariel', 10))
        self.cbutton_s3.place(x=360, y=164)

        self.cbutton_s4 = Checkbutton(self.window, text='Fries ($2)', variable=self.button_s4, font=('Ariel', 10))
        self.cbutton_s4.place(x=360, y=185)

        self.cbutton_s5 = Checkbutton(self.window, text='Onion Rings ($2)', variable=self.button_s5, font=('Ariel', 10))
        self.cbutton_s5.place(x=360, y=204)

        '''
        DRINKS
        ------
        5 drinks for the user to choose from
        IntVars lets the program store the price of the item.
        '''

        self.button_drink1 = IntVar()
        self.button_drink2 = IntVar()
        self.button_drink3 = IntVar()
        self.button_drink4 = IntVar()
        self.button_drink5 = IntVar()

        self.cbutton_drink1 = Checkbutton(self.window, variable = self.button_drink1, text='Pepsi ($2)', font=('Ariel', 10))
        self.cbutton_drink1.place(x=485, y=125)

        self.cbutton_drink2 = Checkbutton(self.window, variable = self.button_drink2,text='Diet Pepsi ($2)', font=('Ariel', 10))
        self.cbutton_drink2.place(x=485, y=145)

        self.cbutton_drink3 = Checkbutton(self.window, variable = self.button_drink3,text='7 up ($2)', font=('Ariel', 10))
        self.cbutton_drink3.place(x=485, y=165)

        self.cbutton_drink4 = Checkbutton(self.window, variable = self.button_drink4,text='Tea ($2)', font=('Ariel', 10))
        self.cbutton_drink4.place(x=485, y=185)

        self.cbutton_drink5 = Checkbutton(self.window, variable = self.button_drink5, text='Mtn Dew ($2)', font=('Ariel', 10))
        self.cbutton_drink5.place(x=485, y=205)

        '''
        DESSERTS
        --------
        5 desserts for the user to choose from
        IntVars lets the program store the price of the item.
        '''

        self.button_des1 = IntVar()
        self.button_des2 = IntVar()
        self.button_des3 = IntVar()
        self.button_des4 = IntVar()
        self.button_des5 = IntVar()

        self.cbutton_des1 = Checkbutton(self.window, variable = self.button_des1, text='Cheesecake ($8)', font=('Ariel', 10))
        self.cbutton_des1.place(x=605, y=125)

        self.cbutton_des2 = Checkbutton(self.window, variable = self.button_des2, text='Chocolate Cake ($8)', font=('Ariel', 10))
        self.cbutton_des2.place(x=605, y=145)

        self.cbutton_des3 = Checkbutton(self.window, variable = self.button_des3, text='Ice Cream ($5)', font=('Ariel', 10))
        self.cbutton_des3.place(x=605, y=165)

        self.cbutton_des4 = Checkbutton(self.window, variable = self.button_des4, text='Tiramisu ($8)', font=('Ariel', 10))
        self.cbutton_des4.place(x=605, y=185)

        self.cbutton_des5 = Checkbutton(self.window, variable = self.button_des5, text='Creme Brulee ($10)', font=('Ariel', 10))
        self.cbutton_des5.place(x=605, y=205)


    def submit(self): #TODO: Finish setting up
        '''

        :return:
        '''

        try:
            self.calc()
            self.name = self.cust_strVar.get()
            self.total_food = self.total_app + self.total_ent + self.total_side + self.total_drink + self.total_des
            if self.total_food == 0 or self.name == '':
                raise ValueError
            else:
                self.tax = self.total_food * 0.10

                if self.tip == 0:
                    pass
                else:
                    self.tip *= self.total_food
                self.total_all += self.tax
                self.total_all += self.tip
                self.total_all += self.total_food
                self.split_bill_calc()


        except:
            self.label_menu_title.config(text='Looks like something went wrong!\nMake sure you selected your items and input your name.')

    # TODO: FIX CLEAR

    def clear(self):
        self.selection.set(1)
        self.bill_split.set(5)

        self.button_a1.set(0)
        self.button_a2.set(0)
        self.button_a3.set(0)

        self.button_e1.set(0)
        self.button_e2.set(0)
        self.button_e3.set(0)
        self.button_e4.set(0)
        self.button_e5.set(0)

        self.button_s1.set(0)
        self.button_s2.set(0)
        self.button_s3.set(0)
        self.button_s4.set(0)
        self.button_s5.set(0)

        self.button_drink1.set(0)
        self.button_drink2.set(0)
        self.button_drink3.set(0)
        self.button_drink4.set(0)
        self.button_drink5.set(0)

        self.button_des1.set(0)
        self.button_des2.set(0)
        self.button_des3.set(0)
        self.button_des4.set(0)
        self.button_des5.set(0)

        self.cust_strVar.set('')

        self.clear_text = StringVar('')

        self.label_menu_title.config(text='Select what you would like to order, and submit it to be completed when ready!')
        self.order_sum.config(text='')
        self.sum_name.config(text='')
        self.sum_total.config(text='')
        self.sum_food.config(text='')
        self.sum_tax.config(text='')
        self.sum_tip.config(text='')

        self.sum_name_input.config(text='')
        self.sum_total_input.config(text='')
        self.sum_food_input.config(text='')
        self.sum_tax_input.config(text='')
        self.sum_tip_input.config(text='')

        self.bill_1.config(text='')
        self.bill_1_food.config(text='')
        self.bill_1_tax.config(text='')
        self.bill_1_tip.config(text='')
        self.bill_1_total_label.config(text='')

        self.bill_2.config(text='')
        self.bill_2_food.config(text='')
        self.bill_2_tax.config(text='')
        self.bill_2_tip.config(text='')
        self.bill_2_total_label.config(text='')

        self.bill_3.config(text='')
        self.bill_3_food.config(text='')
        self.bill_3_tax.config(text='')
        self.bill_3_tip.config(text='')
        self.bill_3_total_label.config(text='')

        self.bill_4.config(text='')
        self.bill_4_food.config(text='')
        self.bill_4_tax.config(text='')
        self.bill_4_tip.config(text='')
        self.bill_4_total_label.config(text='')


    def calc(self):
        self.tip = 0
        selection = self.selection.get()
        if selection == 1:
            self.tip = 0
        if selection == 2:
            self.tip = 0.10
        if selection == 3:
            self.tip = 0.15
        if selection == 4:
            self.tip = 0.20

        self.total_app = 0.0
        self.total_ent = 0.0
        self.total_side = 0.0
        self.total_drink = 0.0
        self.total_des = 0.0
        self.total_food = 0.0
        self.total_all = 0.0

        # CHECKING APPETIZERS SELECTED
        if self.button_a1.get():
            self.total_app += 6.0
        if self.button_a2.get():
            self.total_app += 5.0
        if self.button_a3.get():
            self.total_app += 8.0

        # CHECKING ENTREE SELECTED
        if self.button_e1.get():
            self.total_ent += 35.0
        if self.button_e2.get():
            self.total_ent += 39.0
        if self.button_e3.get():
            self.total_ent += 20.0
        if self.button_e4.get():
            self.total_ent += 30.0
        if self.button_e5.get():
            self.total_ent += 22.0

        # CHECKING SIDES SELECTED
        if self.button_s1.get():
            self.total_side += 2.0
        if self.button_s2.get():
            self.total_side += 2.0
        if self.button_s3.get():
            self.total_side += 3.0
        if self.button_s4.get():
            self.total_side += 2.0
        if self.button_s5.get():
            self.total_side += 2.0

        # CHECKING DRINKS SELECTED
        if self.button_drink1.get():
            self.total_drink += 2.0
        if self.button_drink2.get():
            self.total_drink += 2.0
        if self.button_drink3.get():
            self.total_drink += 2.0
        if self.button_drink4.get():
            self.total_drink += 2.0
        if self.button_drink5.get():
            self.total_drink += 2.0

        # CHECKING DESSERT SELECTION
        if self.button_des1.get():
            self.total_des += 8.0
        if self.button_des2.get():
            self.total_des += 8.0
        if self.button_des3.get():
            self.total_des += 5.0
        if self.button_des4.get():
            self.total_des += 8.0
        if self.button_des5.get():
            self.total_des += 10.0

    def split_bill_calc(self):
        bill_split = self.bill_split.get()
        if bill_split == 5: #TODO: Blank labels overlapping breaking text and going to except above
            if bill_split == 5: #WORKS
                self.order_sum.config(text='Order Summary:')

                self.sum_name.config(text='Customer Name:')

                self.sum_total.config(text='Total:')

                self.sum_food.config(text='Food:')

                self.sum_tax.config(text='Tax:')

                self.sum_tip.config(text=f'Tip:')

                self.sum_name_input.config(text=self.name)

                self.sum_total_input.config(text=(f'{self.total_all:.2f}'))

                self.sum_food_input.config(text=(f'{self.total_food:.2f}'))

                self.sum_tax_input.config(text=(f'{self.tax:.2f}'))

                self.sum_tip_input.config(text=(f'{self.tip:.2f}'))
        elif bill_split == 6:
            self.bill_1_food_total = self.total_food / 2
            self.bill_1_tip_total = self.tip / 2
            self.bill_1_tax_total = self.tax / 2
            self.bill_1_total = self.total_all / 2

            self.order_sum.config(text='Order Summary:')
            self.sum_name.config(text=f'Name: {self.name}')
            self.bill_1.config(text='Bill 1')
            self.bill_1_food.config(text=f'Food: {self.bill_1_food_total:.2f}')
            self.bill_1_tax.config(text=f'Tax: {self.bill_1_tax_total:.2f}')
            self.bill_1_tip.config(text=f'Tip: {self.bill_1_tip_total:.2f}')
            self.bill_1_total_label.config(text=f'Total: {self.bill_1_total:.2f}')

            self.bill_2.config(text='Bill 2')
            self.bill_2_food.config(text=f'Food: {self.bill_1_food_total:.2f}')
            self.bill_2_tax.config(text=f'Tax: {self.bill_1_tax_total:.2f}')
            self.bill_2_tip.config(text=f'Tip: {self.bill_1_tip_total:.2f}')
            self.bill_2_total_label.config(text=f'Total: {self.bill_1_total:.2f}')


        elif bill_split == 7:
            self.bill_1_food_total = self.total_food / 3
            self.bill_1_tip_total = self.tip / 3
            self.bill_1_tax_total = self.tax / 3
            self.bill_1_total = self.total_all / 3

            self.order_sum.config(text='Order Summary:')
            self.sum_name.config(text=f'Name: {self.name}')
            self.bill_1.config(text='Bill 1')
            self.bill_1_food.config(text=f'Food: {self.bill_1_food_total:.2f}')
            self.bill_1_tax.config(text=f'Tax: {self.bill_1_tax_total:.2f}')
            self.bill_1_tip.config(text=f'Tip: {self.bill_1_tip_total:.2f}')
            self.bill_1_total_label.config(text=f'Total: {self.bill_1_total:.2f}')

            self.bill_2.config(text='Bill 2')
            self.bill_2_food.config(text=f'Food: {self.bill_1_food_total:.2f}')
            self.bill_2_tax.config(text=f'Tax: {self.bill_1_tax_total:.2f}')
            self.bill_2_tip.config(text=f'Tip: {self.bill_1_tip_total:.2f}')
            self.bill_2_total_label.config(text=f'Total: {self.bill_1_total:.2f}')

            self.bill_3.config(text='Bill 3')
            self.bill_3_food.config(text=f'Food: {self.bill_1_food_total:.2f}')
            self.bill_3_tax.config(text=f'Tax: {self.bill_1_tax_total:.2f}')
            self.bill_3_tip.config(text=f'Tip: {self.bill_1_tip_total:.2f}')
            self.bill_3_total_label.config(text=f'Total: {self.bill_1_total:.2f}')


        elif bill_split == 8:
            self.bill_1_food_total = self.total_food / 4
            self.bill_1_tip_total = self.tip / 4
            self.bill_1_tax_total = self.tax / 4
            self.bill_1_total = self.total_all / 4

            self.order_sum.config(text='Order Summary:')
            self.sum_name.config(text=f'Name: {self.name}')
            self.bill_1.config(text='Bill 1')
            self.bill_1_food.config(text=f'Food: {self.bill_1_food_total:.2f}')
            self.bill_1_tax.config(text=f'Tax: {self.bill_1_tax_total:.2f}')
            self.bill_1_tip.config(text=f'Tip: {self.bill_1_tip_total:.2f}')
            self.bill_1_total_label.config(text=f'Total: {self.bill_1_total:.2f}')

            self.bill_2.config(text='Bill 2')
            self.bill_2_food.config(text=f'Food: {self.bill_1_food_total:.2f}')
            self.bill_2_tax.config(text=f'Tax: {self.bill_1_tax_total:.2f}')
            self.bill_2_tip.config(text=f'Tip: {self.bill_1_tip_total:.2f}')
            self.bill_2_total_label.config(text=f'Total: {self.bill_1_total:.2f}')

            self.bill_3.config(text='Bill 3')
            self.bill_3_food.config(text=f'Food: {self.bill_1_food_total:.2f}')
            self.bill_3_tax.config(text=f'Tax: {self.bill_1_tax_total:.2f}')
            self.bill_3_tip.config(text=f'Tip: {self.bill_1_tip_total:.2f}')
            self.bill_3_total_label.config(text=f'Total: {self.bill_1_total:.2f}')

            self.bill_4.config(text='Bill 4')
            self.bill_4_food.config(text=f'Food: {self.bill_1_food_total:.2f}')
            self.bill_4_tax.config(text=f'Tax: {self.bill_1_tax_total:.2f}')
            self.bill_4_tip.config(text=f'Tip: {self.bill_1_tip_total:.2f}')
            self.bill_4_total_label.config(text=f'Total: {self.bill_1_total:.2f}')

