import tkinter as tk
import database as db
import re
import smtplib

# Global Variables
TITLE_FONT = ("Courier", 50, "bold")
SEARCH_BAR_FONT = ("Times", 25)
SEARCH_BTN_FONT = ("Times", 14)
CART_BTN_FONT = ("Times", 20)
CATEGORY_BTN_FONT = ("Times", 11)
PRODUCT_NAME_FONT = ("Times", 12)
PURCHASE_FONT = ("Times", 16)
PROMPT_FONT = ("Times", 20)
ITEMS = []
db.populate_items(ITEMS)   # Populate the database
db.randomize_items(ITEMS)  # Randomize the order of the database list
CURRENT_ITEMS = ITEMS
IN_CART = []
NAME = ""
EMAIL = ""
TOTAL = ""


class FrontPage(tk.Frame):
    # Front Page Class
    # Date: 4/5/20
    # Programmer:
    # Description: Organizes the front page, search bar and categories functionality, and display items
    # Data Structures: list

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#F0FFFF")

        # FRAMES
        self.top = tk.Frame(self, bg="#F0FFFF")
        self.top.pack(fill="x")
        self.middle = tk.Frame(self, bg="#F0FFFF")
        self.middle.pack(fill="x", padx="135")
        self.bottom = tk.Frame(self, bg="#F0FFFF")
        self.bottom.pack(fill="x", padx="200")
        self.item1_display = tk.Frame(self.bottom, bg="#F0FFFF", highlightthickness="1",
                                      highlightbackground="black")
        self.item1_display.pack(fill="x")
        self.item2_display = tk.Frame(self.bottom, bg="#F0FFFF", highlightthickness="1",
                                      highlightbackground="black")
        self.item2_display.pack(fill="x")
        self.item3_display = tk.Frame(self.bottom, bg="#F0FFFF", highlightthickness="1",
                                      highlightbackground="black")
        self.item3_display.pack(fill="x")

        # TOP BAR
        title = tk.Label(self.top, text="  j", font=TITLE_FONT, fg="#e53238", bg="#F0FFFF")
        title.pack(pady=10, side="left")
        title = tk.Label(self.top, text="t", font=TITLE_FONT, fg="#0064d2", bg="#F0FFFF")
        title.pack(pady=10, side="left")
        title = tk.Label(self.top, text="a", font=TITLE_FONT, fg="#f5af02", bg="#F0FFFF")
        title.pack(pady=10, side="left")
        title = tk.Label(self.top, text="b", font=TITLE_FONT, fg="#86b817", bg="#F0FFFF")
        title.pack(pady=10, side="left")

        self.search_bar = tk.Entry(self.top, font=SEARCH_BAR_FONT)
        self.search_bar.pack(pady=30, padx=10, side="left")

        self.search_button = tk.Button(self.top, text="Search",
                                       command=lambda: self.search_items(None), font=SEARCH_BTN_FONT)
        self.search_button.pack(pady=24, padx=10, side="left")

        self.cart_button = tk.Button(self.top, text="Cart", font=CART_BTN_FONT,
                                     command=lambda: [controller.show_page(SecondPage),
                                                      SecondPage.update_cart(controller.pages[SecondPage])])
        self.cart_button.pack(pady=24, padx=50, side="left")

        # CATEGORIES
        self.categories = tk.Label(self.middle, text="Categories: ", bg="#F0FFFF",
                                   font=SEARCH_BTN_FONT)
        self.categories.pack(fill="x", side="left")

        self.school_category = tk.Button(self.middle, text="School", font=CATEGORY_BTN_FONT,
                                         command=lambda: self.search_items("school"))
        self.school_category.pack(pady="10", padx="10", side="left")

        self.food_category = tk.Button(self.middle, text="Food", font=CATEGORY_BTN_FONT,
                                       command=lambda: self.search_items("food"))
        self.food_category.pack(pady="10", padx="10", side="left")

        self.tools_category = tk.Button(self.middle, text="Tools", font=CATEGORY_BTN_FONT,
                                        command=lambda: self.search_items("tools"))
        self.tools_category.pack(pady="10", padx="10", side="left")

        self.transport_category = tk.Button(self.middle, text="Transport", font=CATEGORY_BTN_FONT,
                                            command=lambda: self.search_items("transport"))
        self.transport_category.pack(pady="10", padx="10", side="left")

        self.clothes_category = tk.Button(self.middle, text="Clothes", font=CATEGORY_BTN_FONT,
                                          command=lambda: self.search_items("clothes"))
        self.clothes_category.pack(pady="10", padx="10", side="left")

        self.games_category = tk.Button(self.middle, text="Games", font=CATEGORY_BTN_FONT,
                                        command=lambda: self.search_items("games"))
        self.games_category.pack(pady="10", padx="10", side="left")

        self.technology_category = tk.Button(self.middle, text="Technology", font=CATEGORY_BTN_FONT,
                                             command=lambda: self.search_items("technology"))
        self.technology_category.pack(pady="10", padx="10", side="left")

        # NO MATCH
        self.no_search = tk.Label(self.bottom, text="No Items Match Your Search",
                                  bg="#F0FFFF", font=SEARCH_BAR_FONT)

        # PRODUCT 1
        self.photo1 = tk.PhotoImage(file=ITEMS[0].pic)
        self.thumbnail1 = tk.Label(self.item1_display, image=self.photo1, bg="#F0FFFF")
        self.thumbnail1.image = self.photo1
        self.thumbnail1.pack(side="left")

        self.product_name1 = tk.Label(self.item1_display, text=ITEMS[0].name, bg="#F0FFFF",
                                      font=PRODUCT_NAME_FONT)
        self.product_name1.pack(anchor="nw")

        self.product_price1 = tk.Label(self.item1_display, text=ITEMS[0].price, bg="#F0FFFF",
                                       font=PRODUCT_NAME_FONT)
        self.product_price1.pack(anchor="ne")

        self.product_brief1 = tk.Label(self.item1_display, text=ITEMS[0].brief, bg="#F0FFFF",
                                       font=PRODUCT_NAME_FONT)
        self.product_brief1.pack(anchor="w")

        self.add_to_cart1 = tk.Button(self.item1_display, text="Add to Cart", font=PRODUCT_NAME_FONT,
                                      command=lambda: SecondPage.increase(controller.pages[SecondPage],
                                                                          CURRENT_ITEMS[0].name))
        self.add_to_cart1.pack(anchor="e")

        self.expand1 = tk.Button(self.item1_display, text="Read More", font=PRODUCT_NAME_FONT,
                                 command=lambda: self.expand(0))
        self.expand1.pack(anchor="sw")

        # PRODUCT 2
        self.photo2 = tk.PhotoImage(file=ITEMS[1].pic)
        self.thumbnail2 = tk.Label(self.item2_display, image=self.photo2, bg="#F0FFFF")
        self.thumbnail2.image = self.photo2
        self.thumbnail2.pack(side="left")

        self.product_name2 = tk.Label(self.item2_display, text=ITEMS[1].name,
                                      bg="#F0FFFF", font=PRODUCT_NAME_FONT)
        self.product_name2.pack(anchor="nw")

        self.product_price2 = tk.Label(self.item2_display, text=ITEMS[1].price,
                                       bg="#F0FFFF", font=PRODUCT_NAME_FONT)
        self.product_price2.pack(anchor="ne")

        self.product_brief2 = tk.Label(self.item2_display, text=ITEMS[1].brief,
                                       bg="#F0FFFF", font=PRODUCT_NAME_FONT)
        self.product_brief2.pack(anchor="w")

        self.add_to_cart2 = tk.Button(self.item2_display, text="Add to Cart", font=PRODUCT_NAME_FONT,
                                      command=lambda: SecondPage.increase(controller.pages[SecondPage],
                                                                          CURRENT_ITEMS[1].name))
        self.add_to_cart2.pack(anchor="e")

        self.expand2 = tk.Button(self.item2_display, text="Read More", font=PRODUCT_NAME_FONT,
                                 command=lambda: self.expand(1))
        self.expand2.pack(anchor="sw")

        # PRODUCT 3
        self.photo3 = tk.PhotoImage(file=ITEMS[2].pic)
        self.thumbnail3 = tk.Label(self.item3_display, image=self.photo3, bg="#F0FFFF")
        self.thumbnail3.image = self.photo3
        self.thumbnail3.pack(side="left")

        self.product_name3 = tk.Label(self.item3_display, text=ITEMS[2].name, bg="#F0FFFF",
                                      font=PRODUCT_NAME_FONT)
        self.product_name3.pack(anchor="nw")

        self.product_price3 = tk.Label(self.item3_display, text=ITEMS[2].price, bg="#F0FFFF",
                                       font=PRODUCT_NAME_FONT)
        self.product_price3.pack(anchor="ne")

        self.product_brief3 = tk.Label(self.item3_display, text=ITEMS[2].brief, bg="#F0FFFF",
                                       font=PRODUCT_NAME_FONT)
        self.product_brief3.pack(anchor="w")

        self.add_to_cart3 = tk.Button(self.item3_display, text="Add to Cart", font=PRODUCT_NAME_FONT,
                                      command=lambda: SecondPage.increase(controller.pages[SecondPage],
                                                                          CURRENT_ITEMS[2].name))
        self.add_to_cart3.pack(anchor="e")

        self.expand3 = tk.Button(self.item3_display, text="Read More",
                                 font=PRODUCT_NAME_FONT, command=lambda: self.expand(2))
        self.expand3.pack(anchor="sw")

    def search_items(self, category):
        # Search Items
        # Date: 4/5/20
        # Programmer:
        # Description: takes input from search bar or category button and displays
        #              corresponding items
        # Data Structures: lists

        # determine search query
        if category is None:
            words = self.search_bar.get()
        else:
            words = category
        global CURRENT_ITEMS
        CURRENT_ITEMS = []  # clear current items

        # add product to list based on search
        for x in ITEMS:
            if x.name.lower() == words.lower() or x.tag.lower() == words.lower():
                CURRENT_ITEMS.append(x)

        # display items based on search query and clear old items
        if len(CURRENT_ITEMS) == 0:
            self.item1_display.pack_forget()
            self.item2_display.pack_forget()
            self.item3_display.pack_forget()
            self.no_search.pack()
        elif len(CURRENT_ITEMS) == 1:
            self.item1_display.pack(fill="x")
            self.item2_display.pack_forget()
            self.item3_display.pack_forget()
            self.no_search.pack_forget()
            self.product1_repopulate()
        elif len(CURRENT_ITEMS) == 2:
            self.item1_display.pack(fill="x")
            self.item2_display.pack(fill="x")
            self.item3_display.pack_forget()
            self.no_search.pack_forget()
            self.product1_repopulate()
            self.product2_repopulate()
        elif len(CURRENT_ITEMS) == 3:
            self.item1_display.pack(fill="x")
            self.item2_display.pack(fill="x")
            self.item3_display.pack(fill="x")
            self.no_search.pack_forget()
            self.product1_repopulate()
            self.product2_repopulate()
            self.product3_repopulate()

    def expand(self, num):
        # Expand
        # Date: 4/5/20
        # Programmer:
        # Description: shows or hides the full description of an item
        # Data Structures: N/A
        if num == 0:
            if self.expand1.cget("text") == "Read More":
                self.expand1.config(text="Read Less")
                self.product_brief1.config(text=CURRENT_ITEMS[0].full)
            elif self.expand1.cget("text") == "Read Less":
                self.expand1.config(text="Read More")
                self.product_brief1.config(text=CURRENT_ITEMS[0].brief)
        elif num == 1:
            if self.expand2.cget("text") == "Read More":
                self.expand2.config(text="Read Less")
                self.product_brief2.config(text=CURRENT_ITEMS[1].full)
            elif self.expand2.cget("text") == "Read Less":
                self.expand2.config(text="Read More")
                self.product_brief2.config(text=CURRENT_ITEMS[1].brief)
        elif num == 2:
            if self.expand3.cget("text") == "Read More":
                self.expand3.config(text="Read Less")
                self.product_brief3.config(text=CURRENT_ITEMS[2].full)
            elif self.expand3.cget("text") == "Read Less":
                self.expand3.config(text="Read More")
                self.product_brief3.config(text=CURRENT_ITEMS[2].brief)

    # Product Repopulate 1, 2, and 3
    # Date: 4/5/20
    # Programmer:
    # Description: change the values the templates to match the current products
    # Data Structures: N/A
    def product1_repopulate(self):
        global CURRENT_ITEMS
        self.product_name1.config(text=CURRENT_ITEMS[0].name)
        self.product_price1.config(text=CURRENT_ITEMS[0].price)
        self.product_brief1.config(text=CURRENT_ITEMS[0].brief)
        self.photo1.config(file=CURRENT_ITEMS[0].pic)
        self.thumbnail1.config(image=self.photo1)
        self.thumbnail1.image = self.photo1
        self.expand1.config(text="Read More")

    def product2_repopulate(self):
        global CURRENT_ITEMS
        self.product_name2.config(text=CURRENT_ITEMS[1].name)
        self.product_price2.config(text=CURRENT_ITEMS[1].price)
        self.product_brief2.config(text=CURRENT_ITEMS[1].brief)
        self.photo2.config(file=CURRENT_ITEMS[1].pic)
        self.thumbnail2.config(image=self.photo2)
        self.thumbnail2.image = self.photo2
        self.expand2.config(text="Read More")

    def product3_repopulate(self):
        global CURRENT_ITEMS
        self.product_name3.config(text=CURRENT_ITEMS[2].name)
        self.product_price3.config(text=CURRENT_ITEMS[2].price)
        self.product_brief3.config(text=CURRENT_ITEMS[2].brief)
        self.photo3.config(file=CURRENT_ITEMS[2].pic)
        self.thumbnail3.config(image=self.photo3)
        self.thumbnail3.image = self.photo3
        self.expand3.config(text="Read More")


class SecondPage(tk.Frame):
    # Second Page Class
    # Date: 4/6/20
    # Programmer:
    # Description: Display items in cart and the total price; modify amount functionality
    # Data Structures: list

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#F0FFFF")

        # FRAMES
        self.top = tk.Frame(self, bg="#F0FFFF")
        self.top.pack(fill="x")
        self.middle = tk.Frame(self, bg="#F0FFFF")
        self.middle.pack(fill="x", padx="200")
        self.bottom = tk.Frame(self, bg="#F0FFFF")
        self.bottom.pack(fill="x", side="bottom")

        self.cart_title_display = tk.Frame(self.middle, bg="#F0FFFF")
        self.cart_title_display.pack(fill="x")
        self.cart_item1_display = tk.Frame(self.middle, bg="#F0FFFF", highlightthickness="1",
                                           highlightbackground="black")
        self.cart_item1_display.pack(fill="x")
        self.cart_item2_display = tk.Frame(self.middle, bg="#F0FFFF", highlightthickness="1",
                                           highlightbackground="black")
        self.cart_item2_display.pack(fill="x")
        self.cart_item3_display = tk.Frame(self.middle, bg="#F0FFFF", highlightthickness="1",
                                           highlightbackground="black")
        self.cart_item3_display.pack(fill="x")
        self.cart_item4_display = tk.Frame(self.middle, bg="#F0FFFF", highlightthickness="1",
                                           highlightbackground="black")
        self.cart_item4_display.pack(fill="x")
        self.cart_item5_display = tk.Frame(self.middle, bg="#F0FFFF", highlightthickness="1",
                                           highlightbackground="black")
        self.cart_item5_display.pack(fill="x")
        self.cart_item6_display = tk.Frame(self.middle, bg="#F0FFFF", highlightthickness="1",
                                           highlightbackground="black")
        self.cart_item6_display.pack(fill="x")
        self.cart_item7_display = tk.Frame(self.middle, bg="#F0FFFF", highlightthickness="1",
                                           highlightbackground="black")
        self.cart_item7_display.pack(fill="x")
        self.cart_item8_display = tk.Frame(self.middle, bg="#F0FFFF", highlightthickness="1",
                                           highlightbackground="black")
        self.cart_item8_display.pack(fill="x")
        self.cart_item9_display = tk.Frame(self.middle, bg="#F0FFFF", highlightthickness="1",
                                           highlightbackground="black")
        self.cart_item9_display.pack(fill="x")
        self.cart_item10_display = tk.Frame(self.middle, bg="#F0FFFF", highlightthickness="1",
                                            highlightbackground="black")
        self.cart_item10_display.pack(fill="x")
        self.cart_item11_display = tk.Frame(self.middle, bg="#F0FFFF", highlightthickness="1",
                                            highlightbackground="black")
        self.cart_item11_display.pack(fill="x")
        self.cart_item12_display = tk.Frame(self.middle, bg="#F0FFFF", highlightthickness="1",
                                            highlightbackground="black")
        self.cart_item12_display.pack(fill="x")
        self.cart_item13_display = tk.Frame(self.middle, bg="#F0FFFF", highlightthickness="1",
                                            highlightbackground="black")
        self.cart_item13_display.pack(fill="x")
        self.cart_item14_display = tk.Frame(self.middle, bg="#F0FFFF", highlightthickness="1",
                                            highlightbackground="black")
        self.cart_item14_display.pack(fill="x")
        self.cart_item15_display = tk.Frame(self.middle, bg="#F0FFFF", highlightthickness="1",
                                            highlightbackground="black")
        self.cart_item15_display.pack(fill="x")

        # TOP BAR
        self.title = tk.Label(self.top, text="  j", font=TITLE_FONT, fg="#e53238", bg="#F0FFFF")
        self.title.pack(pady=10, side="left")
        self.title = tk.Label(self.top, text="t", font=TITLE_FONT, fg="#0064d2", bg="#F0FFFF")
        self.title.pack(pady=10, side="left")
        self.title = tk.Label(self.top, text="a", font=TITLE_FONT, fg="#f5af02", bg="#F0FFFF")
        self.title.pack(pady=10, side="left")
        self.title = tk.Label(self.top, text="b", font=TITLE_FONT, fg="#86b817", bg="#F0FFFF")
        self.title.pack(pady=10, side="left")

        self.cart_button = tk.Button(self.top, text="Home", font=CART_BTN_FONT,
                                     command=lambda: controller.show_page(FrontPage))
        self.cart_button.pack(pady=24, padx=66, side="right")

        # CART
        self.cart_title = tk.Label(self.cart_title_display, text="Your Cart:", font=PURCHASE_FONT,
                                   bg="#F0FFFF")
        self.cart_title.pack(side="left")
        self.cart_total = tk.Label(self.cart_title_display, text="Total: ", font=PURCHASE_FONT,
                                   bg="#F0FFFF")
        self.cart_total.pack(side="right")

        self.cart_item1 = tk.Label(self.cart_item1_display, text="test", font=PURCHASE_FONT,
                                   bg="#F0FFFF")
        self.cart_item1.pack(side="left")
        self.cart_item2 = tk.Label(self.cart_item2_display, text="test", font=PURCHASE_FONT,
                                   bg="#F0FFFF")
        self.cart_item2.pack(side="left")
        self.cart_item3 = tk.Label(self.cart_item3_display, text="test", font=PURCHASE_FONT,
                                   bg="#F0FFFF")
        self.cart_item3.pack(side="left")
        self.cart_item4 = tk.Label(self.cart_item4_display, text="test", font=PURCHASE_FONT,
                                   bg="#F0FFFF")
        self.cart_item4.pack(side="left")
        self.cart_item5 = tk.Label(self.cart_item5_display, text="test", font=PURCHASE_FONT,
                                   bg="#F0FFFF")
        self.cart_item5.pack(side="left")
        self.cart_item6 = tk.Label(self.cart_item6_display, text="test", font=PURCHASE_FONT,
                                   bg="#F0FFFF")
        self.cart_item6.pack(side="left")
        self.cart_item7 = tk.Label(self.cart_item7_display, text="test", font=PURCHASE_FONT,
                                   bg="#F0FFFF")
        self.cart_item7.pack(side="left")
        self.cart_item8 = tk.Label(self.cart_item8_display, text="test", font=PURCHASE_FONT,
                                   bg="#F0FFFF")
        self.cart_item8.pack(side="left")
        self.cart_item9 = tk.Label(self.cart_item9_display, text="test", font=PURCHASE_FONT,
                                   bg="#F0FFFF")
        self.cart_item9.pack(side="left")
        self.cart_item10 = tk.Label(self.cart_item10_display, text="test", font=PURCHASE_FONT,
                                    bg="#F0FFFF")
        self.cart_item10.pack(side="left")
        self.cart_item11 = tk.Label(self.cart_item11_display, text="test", font=PURCHASE_FONT,
                                    bg="#F0FFFF")
        self.cart_item11.pack(side="left")
        self.cart_item12 = tk.Label(self.cart_item12_display, text="test", font=PURCHASE_FONT,
                                    bg="#F0FFFF")
        self.cart_item12.pack(side="left")
        self.cart_item13 = tk.Label(self.cart_item13_display, text="test", font=PURCHASE_FONT,
                                    bg="#F0FFFF")
        self.cart_item13.pack(side="left")
        self.cart_item14 = tk.Label(self.cart_item14_display, text="test", font=PURCHASE_FONT,
                                    bg="#F0FFFF")
        self.cart_item14.pack(side="left")
        self.cart_item15 = tk.Label(self.cart_item15_display, text="test", font=PURCHASE_FONT,
                                    bg="#F0FFFF")
        self.cart_item15.pack(side="left")

        self.more1 = tk.Button(self.cart_item1_display, text=" + ", font=PRODUCT_NAME_FONT,
                               command=lambda: self.increase(IN_CART[0].name))
        self.more1.pack(side="right")
        self.amount1 = tk.Label(self.cart_item1_display, text=ITEMS[0].in_cart, font=PURCHASE_FONT,
                                bg="#F0FFFF")
        self.amount1.pack(side="right")
        self.less1 = tk.Button(self.cart_item1_display, text=" - ", font=PRODUCT_NAME_FONT,
                               command=lambda: self.decrease(IN_CART[0].name))
        self.less1.pack(anchor="ne")

        self.more2 = tk.Button(self.cart_item2_display, text=" + ", font=PRODUCT_NAME_FONT,
                               command=lambda: self.increase(IN_CART[1].name))
        self.more2.pack(side="right")
        self.amount2 = tk.Label(self.cart_item2_display, text=ITEMS[1].in_cart, font=PURCHASE_FONT,
                                bg="#F0FFFF")
        self.amount2.pack(side="right")
        self.less2 = tk.Button(self.cart_item2_display, text=" - ", font=PRODUCT_NAME_FONT,
                               command=lambda: self.decrease(IN_CART[1].name))
        self.less2.pack(anchor="ne")

        self.more3 = tk.Button(self.cart_item3_display, text=" + ", font=PRODUCT_NAME_FONT,
                               command=lambda: self.increase(IN_CART[2].name))
        self.more3.pack(side="right")
        self.amount3 = tk.Label(self.cart_item3_display, text=ITEMS[2].in_cart, font=PURCHASE_FONT,
                                bg="#F0FFFF")
        self.amount3.pack(side="right")
        self.less3 = tk.Button(self.cart_item3_display, text=" - ", font=PRODUCT_NAME_FONT,
                               command=lambda: self.decrease(IN_CART[2].name))
        self.less3.pack(anchor="ne")

        self.more4 = tk.Button(self.cart_item4_display, text=" + ", font=PRODUCT_NAME_FONT,
                               command=lambda: self.increase(IN_CART[3].name))
        self.more4.pack(side="right")
        self.amount4 = tk.Label(self.cart_item4_display, text=ITEMS[3].in_cart, font=PURCHASE_FONT,
                                bg="#F0FFFF")
        self.amount4.pack(side="right")
        self.less4 = tk.Button(self.cart_item4_display, text=" - ", font=PRODUCT_NAME_FONT,
                               command=lambda: self.decrease(IN_CART[3].name))
        self.less4.pack(anchor="ne")

        self.more5 = tk.Button(self.cart_item5_display, text=" + ", font=PRODUCT_NAME_FONT,
                               command=lambda: self.increase(IN_CART[4].name))
        self.more5.pack(side="right")
        self.amount5 = tk.Label(self.cart_item5_display, text=ITEMS[4].in_cart, font=PURCHASE_FONT,
                                bg="#F0FFFF")
        self.amount5.pack(side="right")
        self.less5 = tk.Button(self.cart_item5_display, text=" - ", font=PRODUCT_NAME_FONT,
                               command=lambda: self.decrease(IN_CART[4].name))
        self.less5.pack(anchor="ne")

        self.more6 = tk.Button(self.cart_item6_display, text=" + ", font=PRODUCT_NAME_FONT,
                               command=lambda: self.increase(IN_CART[5].name))
        self.more6.pack(side="right")
        self.amount6 = tk.Label(self.cart_item6_display, text=ITEMS[5].in_cart, font=PURCHASE_FONT,
                                bg="#F0FFFF")
        self.amount6.pack(side="right")
        self.less6 = tk.Button(self.cart_item6_display, text=" - ", font=PRODUCT_NAME_FONT,
                               command=lambda: self.decrease(IN_CART[5].name))
        self.less6.pack(anchor="ne")

        self.more7 = tk.Button(self.cart_item7_display, text=" + ", font=PRODUCT_NAME_FONT,
                               command=lambda: self.increase(IN_CART[6].name))
        self.more7.pack(side="right")
        self.amount7 = tk.Label(self.cart_item7_display, text=ITEMS[6].in_cart, font=PURCHASE_FONT,
                                bg="#F0FFFF")
        self.amount7.pack(side="right")
        self.less7 = tk.Button(self.cart_item7_display, text=" - ", font=PRODUCT_NAME_FONT,
                               command=lambda: self.decrease(IN_CART[6].name))
        self.less7.pack(anchor="ne")

        self.more8 = tk.Button(self.cart_item8_display, text=" + ", font=PRODUCT_NAME_FONT,
                               command=lambda: self.increase(IN_CART[7].name))
        self.more8.pack(side="right")
        self.amount8 = tk.Label(self.cart_item8_display, text=ITEMS[7].in_cart, font=PURCHASE_FONT,
                                bg="#F0FFFF")
        self.amount8.pack(side="right")
        self.less8 = tk.Button(self.cart_item8_display, text=" - ", font=PRODUCT_NAME_FONT,
                               command=lambda: self.decrease(IN_CART[7].name))
        self.less8.pack(anchor="ne")

        self.more9 = tk.Button(self.cart_item9_display, text=" + ", font=PRODUCT_NAME_FONT,
                               command=lambda: self.increase(IN_CART[8].name))
        self.more9.pack(side="right")
        self.amount9 = tk.Label(self.cart_item9_display, text=ITEMS[8].in_cart, font=PURCHASE_FONT,
                                bg="#F0FFFF")
        self.amount9.pack(side="right")
        self.less9 = tk.Button(self.cart_item9_display, text=" - ", font=PRODUCT_NAME_FONT,
                               command=lambda: self.decrease(IN_CART[8].name))
        self.less9.pack(anchor="ne")

        self.more10 = tk.Button(self.cart_item10_display, text=" + ", font=PRODUCT_NAME_FONT,
                                command=lambda: self.increase(IN_CART[9].name))
        self.more10.pack(side="right")
        self.amount10 = tk.Label(self.cart_item10_display, text=ITEMS[9].in_cart, font=PURCHASE_FONT,
                                 bg="#F0FFFF")
        self.amount10.pack(side="right")
        self.less10 = tk.Button(self.cart_item10_display, text=" - ", font=PRODUCT_NAME_FONT,
                                command=lambda: self.decrease(IN_CART[9].name))
        self.less10.pack(anchor="ne")

        self.more11 = tk.Button(self.cart_item11_display, text=" + ", font=PRODUCT_NAME_FONT,
                                command=lambda: self.increase(IN_CART[10].name))
        self.more11.pack(side="right")
        self.amount11 = tk.Label(self.cart_item11_display, text=ITEMS[10].in_cart, font=PURCHASE_FONT,
                                 bg="#F0FFFF")
        self.amount11.pack(side="right")
        self.less11 = tk.Button(self.cart_item11_display, text=" - ", font=PRODUCT_NAME_FONT,
                                command=lambda: self.decrease(IN_CART[10].name))
        self.less11.pack(anchor="ne")

        self.more12 = tk.Button(self.cart_item12_display, text=" + ", font=PRODUCT_NAME_FONT,
                                command=lambda: self.increase(IN_CART[11].name))
        self.more12.pack(side="right")
        self.amount12 = tk.Label(self.cart_item12_display, text=ITEMS[11].in_cart, font=PURCHASE_FONT,
                                 bg="#F0FFFF")
        self.amount12.pack(side="right")
        self.less12 = tk.Button(self.cart_item12_display, text=" - ", font=PRODUCT_NAME_FONT,
                                command=lambda: self.decrease(IN_CART[11].name))
        self.less12.pack(anchor="ne")

        self.more13 = tk.Button(self.cart_item13_display, text=" + ", font=PRODUCT_NAME_FONT,
                                command=lambda: self.increase(IN_CART[12].name))
        self.more13.pack(side="right")
        self.amount13 = tk.Label(self.cart_item13_display, text=ITEMS[12].in_cart, font=PURCHASE_FONT,
                                 bg="#F0FFFF")
        self.amount13.pack(side="right")
        self.less13 = tk.Button(self.cart_item13_display, text=" - ", font=PRODUCT_NAME_FONT,
                                command=lambda: self.decrease(IN_CART[12].name))
        self.less13.pack(anchor="ne")

        self.more14 = tk.Button(self.cart_item14_display, text=" + ", font=PRODUCT_NAME_FONT,
                                command=lambda: self.increase(IN_CART[13].name))
        self.more14.pack(side="right")
        self.amount14 = tk.Label(self.cart_item14_display, text=ITEMS[13].in_cart, font=PURCHASE_FONT,
                                 bg="#F0FFFF")
        self.amount14.pack(side="right")
        self.less14 = tk.Button(self.cart_item14_display, text=" - ", font=PRODUCT_NAME_FONT,
                                command=lambda: self.decrease(IN_CART[13].name))
        self.less14.pack(anchor="ne")

        self.more15 = tk.Button(self.cart_item15_display, text=" + ", font=PRODUCT_NAME_FONT,
                                command=lambda: self.increase(IN_CART[14].name))
        self.more15.pack(side="right")
        self.amount15 = tk.Label(self.cart_item15_display, text=ITEMS[14].in_cart, font=PURCHASE_FONT,
                                 bg="#F0FFFF")
        self.amount15.pack(side="right")
        self.less15 = tk.Button(self.cart_item15_display, text=" - ", font=PRODUCT_NAME_FONT,
                                command=lambda: self.decrease(IN_CART[14].name))
        self.less15.pack(anchor="ne")

        # BOTTOM
        self.purchase_button = tk.Button(self.bottom, text="Purchase", font=PURCHASE_FONT,
                                         command=lambda: controller.show_page(ThirdPage))
        self.purchase_button.pack(pady="10")

    def update_cart(self):
        # Update Cart
        # Date: 4/6/20
        # Programmer:
        # Description: updates and displays the items currently in the cart
        # Data Structures: N/A
        global IN_CART
        IN_CART = []     # empties cart
        for x in ITEMS:  # repopulates cart
            if x.in_cart > 0:
                IN_CART.append(x)

        # displays the updated items in the cart and clears the old ones
        if len(IN_CART) == 0:
            self.cart_item1_display.pack_forget()
            self.cart_item2_display.pack_forget()
            self.cart_item3_display.pack_forget()
            self.cart_item4_display.pack_forget()
            self.cart_item5_display.pack_forget()
            self.cart_item6_display.pack_forget()
            self.cart_item7_display.pack_forget()
            self.cart_item8_display.pack_forget()
            self.cart_item9_display.pack_forget()
            self.cart_item10_display.pack_forget()
            self.cart_item11_display.pack_forget()
            self.cart_item12_display.pack_forget()
            self.cart_item13_display.pack_forget()
            self.cart_item14_display.pack_forget()
            self.cart_item15_display.pack_forget()
            self.purchase_button.pack_forget()
        elif len(IN_CART) == 1:
            self.cart_item2_display.pack_forget()
            self.cart_item3_display.pack_forget()
            self.cart_item4_display.pack_forget()
            self.cart_item5_display.pack_forget()
            self.cart_item6_display.pack_forget()
            self.cart_item7_display.pack_forget()
            self.cart_item8_display.pack_forget()
            self.cart_item9_display.pack_forget()
            self.cart_item10_display.pack_forget()
            self.cart_item11_display.pack_forget()
            self.cart_item12_display.pack_forget()
            self.cart_item13_display.pack_forget()
            self.cart_item14_display.pack_forget()
            self.cart_item15_display.pack_forget()
            self.cart1_repopulate()
            self.purchase_button.pack(pady="10")
        elif len(IN_CART) == 2:
            self.cart_item3_display.pack_forget()
            self.cart_item4_display.pack_forget()
            self.cart_item5_display.pack_forget()
            self.cart_item6_display.pack_forget()
            self.cart_item7_display.pack_forget()
            self.cart_item8_display.pack_forget()
            self.cart_item9_display.pack_forget()
            self.cart_item10_display.pack_forget()
            self.cart_item11_display.pack_forget()
            self.cart_item12_display.pack_forget()
            self.cart_item13_display.pack_forget()
            self.cart_item14_display.pack_forget()
            self.cart_item15_display.pack_forget()
            self.cart1_repopulate()
            self.cart2_repopulate()
            self.purchase_button.pack(pady="10")
        elif len(IN_CART) == 3:
            self.cart_item4_display.pack_forget()
            self.cart_item5_display.pack_forget()
            self.cart_item6_display.pack_forget()
            self.cart_item7_display.pack_forget()
            self.cart_item8_display.pack_forget()
            self.cart_item9_display.pack_forget()
            self.cart_item10_display.pack_forget()
            self.cart_item11_display.pack_forget()
            self.cart_item12_display.pack_forget()
            self.cart_item13_display.pack_forget()
            self.cart_item14_display.pack_forget()
            self.cart_item15_display.pack_forget()
            self.cart1_repopulate()
            self.cart2_repopulate()
            self.cart3_repopulate()
            self.purchase_button.pack(pady="10")
        elif len(IN_CART) == 4:
            self.cart_item5_display.pack_forget()
            self.cart_item6_display.pack_forget()
            self.cart_item7_display.pack_forget()
            self.cart_item8_display.pack_forget()
            self.cart_item9_display.pack_forget()
            self.cart_item10_display.pack_forget()
            self.cart_item11_display.pack_forget()
            self.cart_item12_display.pack_forget()
            self.cart_item13_display.pack_forget()
            self.cart_item14_display.pack_forget()
            self.cart_item15_display.pack_forget()
            self.cart1_repopulate()
            self.cart2_repopulate()
            self.cart3_repopulate()
            self.cart4_repopulate()
            self.purchase_button.pack(pady="10")
        elif len(IN_CART) == 5:
            self.cart_item6_display.pack_forget()
            self.cart_item7_display.pack_forget()
            self.cart_item8_display.pack_forget()
            self.cart_item9_display.pack_forget()
            self.cart_item10_display.pack_forget()
            self.cart_item11_display.pack_forget()
            self.cart_item12_display.pack_forget()
            self.cart_item13_display.pack_forget()
            self.cart_item14_display.pack_forget()
            self.cart_item15_display.pack_forget()
            self.cart1_repopulate()
            self.cart2_repopulate()
            self.cart3_repopulate()
            self.cart4_repopulate()
            self.cart5_repopulate()
            self.purchase_button.pack(pady="10")
        elif len(IN_CART) == 6:
            self.cart_item7_display.pack_forget()
            self.cart_item8_display.pack_forget()
            self.cart_item9_display.pack_forget()
            self.cart_item10_display.pack_forget()
            self.cart_item11_display.pack_forget()
            self.cart_item12_display.pack_forget()
            self.cart_item13_display.pack_forget()
            self.cart_item14_display.pack_forget()
            self.cart_item15_display.pack_forget()
            self.cart1_repopulate()
            self.cart2_repopulate()
            self.cart3_repopulate()
            self.cart4_repopulate()
            self.cart5_repopulate()
            self.cart6_repopulate()
            self.purchase_button.pack(pady="10")
        elif len(IN_CART) == 7:
            self.cart_item8_display.pack_forget()
            self.cart_item9_display.pack_forget()
            self.cart_item10_display.pack_forget()
            self.cart_item11_display.pack_forget()
            self.cart_item12_display.pack_forget()
            self.cart_item13_display.pack_forget()
            self.cart_item14_display.pack_forget()
            self.cart_item15_display.pack_forget()
            self.cart1_repopulate()
            self.cart2_repopulate()
            self.cart3_repopulate()
            self.cart4_repopulate()
            self.cart5_repopulate()
            self.cart6_repopulate()
            self.cart7_repopulate()
            self.purchase_button.pack(pady="10")
        elif len(IN_CART) == 8:
            self.cart_item9_display.pack_forget()
            self.cart_item10_display.pack_forget()
            self.cart_item11_display.pack_forget()
            self.cart_item12_display.pack_forget()
            self.cart_item13_display.pack_forget()
            self.cart_item14_display.pack_forget()
            self.cart_item15_display.pack_forget()
            self.cart1_repopulate()
            self.cart2_repopulate()
            self.cart3_repopulate()
            self.cart4_repopulate()
            self.cart5_repopulate()
            self.cart6_repopulate()
            self.cart7_repopulate()
            self.cart8_repopulate()
            self.purchase_button.pack(pady="10")
        elif len(IN_CART) == 9:
            self.cart_item10_display.pack_forget()
            self.cart_item11_display.pack_forget()
            self.cart_item12_display.pack_forget()
            self.cart_item13_display.pack_forget()
            self.cart_item14_display.pack_forget()
            self.cart_item15_display.pack_forget()
            self.cart1_repopulate()
            self.cart2_repopulate()
            self.cart3_repopulate()
            self.cart4_repopulate()
            self.cart5_repopulate()
            self.cart6_repopulate()
            self.cart7_repopulate()
            self.cart8_repopulate()
            self.cart9_repopulate()
            self.purchase_button.pack(pady="10")
        elif len(IN_CART) == 10:
            self.cart_item11_display.pack_forget()
            self.cart_item12_display.pack_forget()
            self.cart_item13_display.pack_forget()
            self.cart_item14_display.pack_forget()
            self.cart_item15_display.pack_forget()
            self.cart1_repopulate()
            self.cart2_repopulate()
            self.cart3_repopulate()
            self.cart4_repopulate()
            self.cart5_repopulate()
            self.cart6_repopulate()
            self.cart7_repopulate()
            self.cart8_repopulate()
            self.cart9_repopulate()
            self.cart10_repopulate()
            self.purchase_button.pack(pady="10")
        elif len(IN_CART) == 11:
            self.cart_item12_display.pack_forget()
            self.cart_item13_display.pack_forget()
            self.cart_item14_display.pack_forget()
            self.cart_item15_display.pack_forget()
            self.cart1_repopulate()
            self.cart2_repopulate()
            self.cart3_repopulate()
            self.cart4_repopulate()
            self.cart5_repopulate()
            self.cart6_repopulate()
            self.cart7_repopulate()
            self.cart8_repopulate()
            self.cart9_repopulate()
            self.cart10_repopulate()
            self.cart11_repopulate()
            self.purchase_button.pack(pady="10")
        elif len(IN_CART) == 12:
            self.cart_item13_display.pack_forget()
            self.cart_item14_display.pack_forget()
            self.cart_item15_display.pack_forget()
            self.cart1_repopulate()
            self.cart2_repopulate()
            self.cart3_repopulate()
            self.cart4_repopulate()
            self.cart5_repopulate()
            self.cart6_repopulate()
            self.cart7_repopulate()
            self.cart8_repopulate()
            self.cart9_repopulate()
            self.cart10_repopulate()
            self.cart11_repopulate()
            self.cart12_repopulate()
            self.purchase_button.pack(pady="10")
        elif len(IN_CART) == 13:
            self.cart_item14_display.pack_forget()
            self.cart_item15_display.pack_forget()
            self.cart1_repopulate()
            self.cart2_repopulate()
            self.cart3_repopulate()
            self.cart4_repopulate()
            self.cart5_repopulate()
            self.cart6_repopulate()
            self.cart7_repopulate()
            self.cart8_repopulate()
            self.cart9_repopulate()
            self.cart10_repopulate()
            self.cart11_repopulate()
            self.cart12_repopulate()
            self.cart13_repopulate()
            self.purchase_button.pack(pady="10")
        elif len(IN_CART) == 14:
            self.cart_item15_display.pack_forget()
            self.cart1_repopulate()
            self.cart2_repopulate()
            self.cart3_repopulate()
            self.cart4_repopulate()
            self.cart5_repopulate()
            self.cart6_repopulate()
            self.cart7_repopulate()
            self.cart8_repopulate()
            self.cart9_repopulate()
            self.cart10_repopulate()
            self.cart11_repopulate()
            self.cart12_repopulate()
            self.cart13_repopulate()
            self.cart14_repopulate()
            self.purchase_button.pack(pady="10")
        elif len(IN_CART) == 15:
            self.cart1_repopulate()
            self.cart2_repopulate()
            self.cart3_repopulate()
            self.cart4_repopulate()
            self.cart5_repopulate()
            self.cart6_repopulate()
            self.cart7_repopulate()
            self.cart8_repopulate()
            self.cart9_repopulate()
            self.cart10_repopulate()
            self.cart11_repopulate()
            self.cart12_repopulate()
            self.cart13_repopulate()
            self.cart14_repopulate()
            self.cart15_repopulate()
            self.purchase_button.pack(pady="10")
        self.calc_total()

    # Cart Repopulate 1-15
    # Date: 4/6/20
    # Programmer:
    # Description: updates the content in the cart frames
    # Data Structures: N/A
    def cart1_repopulate(self):
        self.cart_item1_display.pack(fill="x")
        self.cart_item1.config(text=IN_CART[0].name)
        self.amount1.config(text=IN_CART[0].in_cart)

    def cart2_repopulate(self):
        self.cart_item2_display.pack(fill="x")
        self.cart_item2.config(text=IN_CART[1].name)
        self.amount2.config(text=IN_CART[1].in_cart)

    def cart3_repopulate(self):
        self.cart_item3_display.pack(fill="x")
        self.cart_item3.config(text=IN_CART[2].name)
        self.amount3.config(text=IN_CART[2].in_cart)

    def cart4_repopulate(self):
        self.cart_item4_display.pack(fill="x")
        self.cart_item4.config(text=IN_CART[3].name)
        self.amount4.config(text=IN_CART[3].in_cart)

    def cart5_repopulate(self):
        self.cart_item5_display.pack(fill="x")
        self.cart_item5.config(text=IN_CART[4].name)
        self.amount5.config(text=IN_CART[4].in_cart)

    def cart6_repopulate(self):
        self.cart_item6_display.pack(fill="x")
        self.cart_item6.config(text=IN_CART[5].name)
        self.amount6.config(text=IN_CART[5].in_cart)

    def cart7_repopulate(self):
        self.cart_item7_display.pack(fill="x")
        self.cart_item7.config(text=IN_CART[6].name)
        self.amount7.config(text=IN_CART[6].in_cart)

    def cart8_repopulate(self):
        self.cart_item8_display.pack(fill="x")
        self.cart_item8.config(text=IN_CART[7].name)
        self.amount8.config(text=IN_CART[7].in_cart)

    def cart9_repopulate(self):
        self.cart_item9_display.pack(fill="x")
        self.cart_item9.config(text=IN_CART[8].name)
        self.amount9.config(text=IN_CART[8].in_cart)

    def cart10_repopulate(self):
        self.cart_item10_display.pack(fill="x")
        self.cart_item10.config(text=IN_CART[9].name)
        self.amount10.config(text=IN_CART[9].in_cart)

    def cart11_repopulate(self):
        self.cart_item11_display.pack(fill="x")
        self.cart_item11.config(text=IN_CART[10].name)
        self.amount11.config(text=IN_CART[10].in_cart)

    def cart12_repopulate(self):
        self.cart_item12_display.pack(fill="x")
        self.cart_item12.config(text=IN_CART[11].name)
        self.amount12.config(text=IN_CART[11].in_cart)

    def cart13_repopulate(self):
        self.cart_item13_display.pack(fill="x")
        self.cart_item13.config(text=IN_CART[12].name)
        self.amount13.config(text=IN_CART[12].in_cart)

    def cart14_repopulate(self):
        self.cart_item14_display.pack(fill="x")
        self.cart_item14.config(text=IN_CART[13].name)
        self.amount14.config(text=IN_CART[13].in_cart)

    def cart15_repopulate(self):
        self.cart_item15_display.pack(fill="x")
        self.cart_item15.config(text=IN_CART[14].name)
        self.amount15.config(text=IN_CART[14].in_cart)

    # Increase and Decrease
    # Date: 4/6/20
    # Programmer:
    # Description: increments and decrements the count of items in cart
    # Data Structures: list
    def increase(self, name):
        for x in ITEMS:
            if x.name == name:
                x.in_cart += 1
        self.update_cart()

    def decrease(self, name):
        for x in ITEMS:
            if x.name == name:
                x.in_cart -= 1
        self.update_cart()

    # Update Cart
    # Date: 4/6/20
    # Programmer:
    # Description: calculates the price total of all items in cart and displays it
    # Data Structures: list
    def calc_total(self):
        global TOTAL
        total = 0
        for x in IN_CART:
            total += (x.in_cart * x.price)
        TOTAL = total
        self.cart_total.config(text="Total: $" + str("{0:.2f}".format(total)))


class ThirdPage(tk.Frame):
    # Third Page
    # Date: 4/7/20
    # Programmer:
    # Description: displays payment card prompt and takes input
    # Data Structures: N/A

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#F0FFFF")

        # FRAMES
        self.top = tk.Frame(self, bg="#F0FFFF")
        self.top.pack(fill="x")
        self.middle = tk.Frame(self, bg="#F0FFFF")
        self.middle.pack(fill="x", padx="180")
        self.bottom = tk.Frame(self, bg="#F0FFFF")
        self.bottom.pack(fill="x", side="bottom")

        self.prompt_display = tk.Frame(self, bg="#F0FFFF")
        self.prompt_display.pack(fill="x", pady="10", padx="180")
        self.card_number_display = tk.Frame(self, bg="#F0FFFF")
        self.card_number_display.pack(fill="x", pady="10", padx="180")
        self.expiration_display = tk.Frame(self, bg="#F0FFFF")
        self.expiration_display.pack(fill="x", pady="10", padx="180")
        self.cvv_display = tk.Frame(self, bg="#F0FFFF")
        self.cvv_display.pack(fill="x", pady="10", padx="180")

        # TOP BAR
        self.title = tk.Label(self.top, text="  j", font=TITLE_FONT, fg="#e53238", bg="#F0FFFF")
        self.title.pack(pady=10, side="left")
        self.title = tk.Label(self.top, text="t", font=TITLE_FONT, fg="#0064d2", bg="#F0FFFF")
        self.title.pack(pady=10, side="left")
        self.title = tk.Label(self.top, text="a", font=TITLE_FONT, fg="#f5af02", bg="#F0FFFF")
        self.title.pack(pady=10, side="left")
        self.title = tk.Label(self.top, text="b", font=TITLE_FONT, fg="#86b817", bg="#F0FFFF")
        self.title.pack(pady=10, side="left")

        # MIDDLE
        self.prompt = tk.Label(self.prompt_display, text="Card Info:   ",
                               font=PROMPT_FONT, bg="#F0FFFF")
        self.prompt.pack(side="left")

        self.error = tk.Label(self.prompt_display, font=PROMPT_FONT, bg="#F0FFFF")
        self.error.pack(side="left")

        self.card_number_prompt = tk.Label(self.card_number_display, text="Enter Card Number: ",
                                           bg="#F0FFFF", font=PROMPT_FONT)
        self.card_number_prompt.pack(side="left")
        self.expiration_prompt = tk.Label(self.expiration_display, text="Enter Expiration Date: ",
                                          bg="#F0FFFF", font=PROMPT_FONT)
        self.expiration_prompt.pack(side="left")
        self.cvv_prompt = tk.Label(self.cvv_display, text="Enter CVV: ", bg="#F0FFFF", font=PROMPT_FONT)
        self.cvv_prompt.pack(side="left")

        self.card_number_entry1 = tk.Entry(self.card_number_display, font=PROMPT_FONT, width="4")
        self.card_number_entry1.pack(padx="8", side="left")
        self.card_number_entry2 = tk.Entry(self.card_number_display, font=PROMPT_FONT, width="4")
        self.card_number_entry2.pack(padx="8", side="left")
        self.card_number_entry3 = tk.Entry(self.card_number_display, font=PROMPT_FONT, width="4")
        self.card_number_entry3.pack(padx="8", side="left")
        self.card_number_entry4 = tk.Entry(self.card_number_display, font=PROMPT_FONT, width="4")
        self.card_number_entry4.pack(padx="8", side="left")

        self.expiration_entry1 = tk.Entry(self.expiration_display, font=PROMPT_FONT, width="2")
        self.expiration_entry1.pack(padx="8", side="left")
        self.slash = tk.Label(self.expiration_display, text="/", font=PROMPT_FONT, bg="#F0FFFF")
        self.slash.pack(side="left")
        self.expiration_entry2 = tk.Entry(self.expiration_display, font=PROMPT_FONT, width="2")
        self.expiration_entry2.pack(padx="8", side="left")

        self.cvv_entry = tk.Entry(self.cvv_display, font=PROMPT_FONT, width="3")
        self.cvv_entry.pack(padx="8", side="left")

        # BOTTOM
        self.continue_button = tk.Button(self.bottom, text="Continue", font=PURCHASE_FONT,
                                         command=lambda: [self.check_error(controller),
                                                          self.clear_entry()])
        self.continue_button.pack(pady="10")

    # Check error and Check card input
    # Date: 4/7/20
    # Programmer:
    # Description: Checks for valid input for the payment card
    # Data Structures: N/A
    def check_error(self, controller):
        card1 = self.card_number_entry1.get()
        card2 = self.card_number_entry2.get()
        card3 = self.card_number_entry3.get()
        card4 = self.card_number_entry4.get()

        expiration1 = self.expiration_entry1.get()
        expiration2 = self.expiration_entry2.get()

        cvv = self.cvv_entry.get()

        # checks for correct amount of numbers entered in each field
        if (self.check_card_valid(card1, 4) and self.check_card_valid(card2, 4)
            and self.check_card_valid(card3, 4) and self.check_card_valid(card4, 4)
                and self.check_card_valid(expiration1, 2) and self.check_card_valid(expiration2, 2)
                and self.check_card_valid(cvv, 3)):
            self.error.config(text=" ")
            controller.show_page(FourthPage)
        else:
            self.error.config(text="Input Valid Card Info")  # error prompt
        return 0

    def check_card_valid(self, length, num):
        # checks if only numbers entered
        if not len(length) == num:
            return False
        for x in length:
            if not x.isnumeric():
                return False
        return True

    # Clear Entry
    # Date: 4/7/20
    # Programmer:
    # Description: Clears entry fields
    # Data Structures: N/A
    def clear_entry(self):
        self.card_number_entry1.delete(0, "end")
        self.card_number_entry2.delete(0, "end")
        self.card_number_entry3.delete(0, "end")
        self.card_number_entry4.delete(0, "end")
        self.expiration_entry1.delete(0, "end")
        self.expiration_entry2.delete(0, "end")
        self.cvv_entry.delete(0, "end")


class FourthPage(tk.Frame):
    # Fourth Page
    # Date: 4/7/20
    # Programmer:
    # Description: displays personal info prompt and takes input
    # Data Structures: N/A

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#F0FFFF")

        # FRAMES
        self.top = tk.Frame(self, bg="#F0FFFF")
        self.top.pack(fill="x")
        self.middle = tk.Frame(self, bg="#F0FFFF")
        self.middle.pack(fill="x", padx="180")
        self.bottom = tk.Frame(self, bg="#F0FFFF")
        self.bottom.pack(fill="x", side="bottom")

        self.prompt_display = tk.Frame(self, bg="#F0FFFF")
        self.prompt_display.pack(fill="x", pady="10", padx="180")
        self.name_display = tk.Frame(self, bg="#F0FFFF")
        self.name_display.pack(fill="x", pady="10", padx="180")
        self.email_display = tk.Frame(self, bg="#F0FFFF")
        self.email_display.pack(fill="x", pady="10", padx="180")
        self.address_display1 = tk.Frame(self, bg="#F0FFFF")
        self.address_display1.pack(fill="x", pady="10", padx="180")
        self.address_display2 = tk.Frame(self, bg="#F0FFFF")
        self.address_display2.pack(fill="x", pady="10", padx="180")
        self.address_display3 = tk.Frame(self, bg="#F0FFFF")
        self.address_display3.pack(fill="x", pady="10", padx="180")

        # TOP BAR
        self.title = tk.Label(self.top, text="  j", font=TITLE_FONT, fg="#e53238", bg="#F0FFFF")
        self.title.pack(pady=10, side="left")
        self.title = tk.Label(self.top, text="t", font=TITLE_FONT, fg="#0064d2", bg="#F0FFFF")
        self.title.pack(pady=10, side="left")
        self.title = tk.Label(self.top, text="a", font=TITLE_FONT, fg="#f5af02", bg="#F0FFFF")
        self.title.pack(pady=10, side="left")
        self.title = tk.Label(self.top, text="b", font=TITLE_FONT, fg="#86b817", bg="#F0FFFF")
        self.title.pack(pady=10, side="left")

        # MIDDLE
        self.prompt = tk.Label(self.prompt_display, text="Personal Info:   ",
                               font=PROMPT_FONT, bg="#F0FFFF")
        self.prompt.pack(side="left")

        self.error = tk.Label(self.prompt_display, font=PROMPT_FONT, bg="#F0FFFF")
        self.error.pack(side="left")

        self.name_prompt = tk.Label(self.name_display, text="Enter Your Name: ",
                                    bg="#F0FFFF", font=PROMPT_FONT)
        self.name_prompt.pack(side="left")
        self.email_prompt = tk.Label(self.email_display, text="Enter Your Email: ",
                                     bg="#F0FFFF", font=PROMPT_FONT)
        self.email_prompt.pack(side="left")
        self.street_prompt = tk.Label(self.address_display1, text="Enter Street Address: ",
                                     bg="#F0FFFF", font=PROMPT_FONT)
        self.street_prompt.pack(side="left")
        self.city_prompt = tk.Label(self.address_display2, text="Enter City: ",
                                      bg="#F0FFFF", font=PROMPT_FONT)
        self.city_prompt.pack(side="left")
        self.zip_prompt = tk.Label(self.address_display3, text="Enter Zip Code: ",
                                   bg="#F0FFFF", font=PROMPT_FONT)
        self.zip_prompt.pack(side="left")

        self.name_entry = tk.Entry(self.name_display, font=PROMPT_FONT)
        self.name_entry.pack(padx="8", side="left")

        self.email_entry = tk.Entry(self.email_display, font=PROMPT_FONT)
        self.email_entry.pack(padx="8", side="left")

        self.street_entry = tk.Entry(self.address_display1, font=PROMPT_FONT)
        self.street_entry.pack(padx="8", side="left")

        self.city_entry = tk.Entry(self.address_display2, font=PROMPT_FONT)
        self.city_entry.pack(padx="8", side="left")

        self.zip_entry = tk.Entry(self.address_display3, font=PROMPT_FONT, width="5")
        self.zip_entry.pack(padx="8", side="left")
        self.state_prompt = tk.Label(self.address_display3, text="Enter State: ",
                                     bg="#F0FFFF", font=PROMPT_FONT)
        self.state_prompt.pack(side="left")
        self.state_entry = tk.Entry(self.address_display3, font=PROMPT_FONT, width="3")
        self.state_entry.pack(padx="8", side="left")

        # BOTTOM
        self.finish_button = tk.Button(self.bottom, text="Finish Purchase", font=PURCHASE_FONT,
                                       command=lambda: [self.check_valid(controller),
                                                        self.clear_entry()])
        self.finish_button.pack(pady="10")

    def check_valid(self, controller):
        # Check Valid
        # Date: 4/7/20
        # Programmer:
        # Description: checks if entered email is formatted correctly
        # Data Structures: N/A
        email = self.email_entry.get()
        valid = "^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$"

        # checks for every input field filled in
        if (re.search(valid, email) and len(self.name_entry.get()) > 0
                and len(self.street_entry.get()) > 0 and len(self.city_entry.get()) > 0
                and len(self.zip_entry.get()) > 0 and len(self.state_entry.get()) > 0):
            self.error.config(text=" ")
            controller.show_page(FifthPage)
            self.save_name_and_email()
            self.send_email()
        else:
            self.error.config(text="Input Valid Email")

    def clear_entry(self):
        # Clear Entry
        # Date: 4/7/20
        # Programmer:
        # Description: clears all input fields
        # Data Structures: N/A
        self.name_entry.delete(0, "end")
        self.email_entry.delete(0, "end")
        self.street_entry.delete(0, "end")
        self.city_entry.delete(0, "end")
        self.zip_entry.delete(0, "end")
        self.state_entry.delete(0, "end")

    def save_name_and_email(self):
        # Save Name and Email
        # Date: 4/7/20
        # Programmer:
        # Description: saves name and email in global variable for later use
        # Data Structures: N/A
        global NAME
        global EMAIL
        NAME = self.name_entry.get()
        EMAIL = self.email_entry.get()

    def send_email(self):
        # Send Email
        # Date: 4/7/20
        # Programmer:
        # Description: sends a conformation email to user
        # Data Structures: N/A
        sender = "jtabecommerce@gmail.com"
        password = "password362"
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to the server
        server.starttls()  # Use TLS
        server.login(sender, password)  # Login to the email server
        server.sendmail(sender, EMAIL, "Thank you for your purchase, " + NAME + ". Your card has been charged for $" + str("{0:.2f}".format(float(TOTAL))))  # Send the email
        server.quit()  # Logout of the email server


class FifthPage(tk.Frame):
    # Fifth Page
    # Date: 4/7/20
    # Programmer:
    # Description: displays a thank you message
    # Data Structures: N/A

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#F0FFFF")

        # FRAMES
        self.top = tk.Frame(self, bg="#F0FFFF")
        self.top.pack(fill="x")
        self.bottom = tk.Frame(self, bg="#F0FFFF")
        self.bottom.pack(fill="x")

        # TOP BAR
        self.title = tk.Label(self.top, text="  j", font=TITLE_FONT, fg="#e53238", bg="#F0FFFF")
        self.title.pack(pady=10, side="left")
        self.title = tk.Label(self.top, text="t", font=TITLE_FONT, fg="#0064d2", bg="#F0FFFF")
        self.title.pack(pady=10, side="left")
        self.title = tk.Label(self.top, text="a", font=TITLE_FONT, fg="#f5af02", bg="#F0FFFF")
        self.title.pack(pady=10, side="left")
        self.title = tk.Label(self.top, text="b", font=TITLE_FONT, fg="#86b817", bg="#F0FFFF")
        self.title.pack(pady=10, side="left")

        self.cart_button = tk.Button(self.top, text="Home", font=CART_BTN_FONT,
                                     command=lambda: [controller.show_page(FrontPage), self.clear_cart()])
        self.cart_button.pack(pady=24, padx=66, side="right")

        # BOTTOM
        self.prompt = tk.Label(self.bottom,
                               text="Thank You For Your Purchase.\nA Email Reciept Has Been Sent.",
                               font=PROMPT_FONT, bg="#F0FFFF")
        self.prompt.pack()

    def clear_cart(self):
        # Clear Cart
        # Date: 4/7/20
        # Programmer:
        # Description: Empties all the items in the cart
        # Data Structures: list
        for x in ITEMS:
            x.in_cart = 0
