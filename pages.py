import tkinter as tk
from tkinter import ttk
import database as db


TITLE_FONT = ("Courier", 50, "bold")
SEARCH_BAR_FONT = ("Times", 25)
SEARCH_BTN_FONT = ("Times", 14)
CART_BTN_FONT = ("Times", 20)
CATEGORY_BTN_FONT = ("Times", 11)
PRODUCT_NAME_FONT = ("Times", 12)
ITEMS = []
db.populate_items(ITEMS)
db.randomize_items(ITEMS)
CURRENT_ITEMS = ITEMS


class FrontPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="#F0FFFF")

        # FRAMES
        self.top = tk.Frame(self, bg="#F0FFFF")
        self.top.pack()
        self.middle = tk.Frame(self, bg="#F0FFFF")
        self.middle.pack(fill="x", padx="135")
        self.bottom = tk.Frame(self, bg="#F0FFFF")
        self.bottom.pack(fill="x", padx="200")
        self.item1_display = tk.Frame(self.bottom, bg="#F0FFFF", highlightthickness="1", highlightbackground="black")
        self.item1_display.pack(fill="x")
        self.item2_display = tk.Frame(self.bottom, bg="#F0FFFF", highlightthickness="1", highlightbackground="black")
        self.item2_display.pack(fill="x")
        self.item3_display = tk.Frame(self.bottom, bg="#F0FFFF", highlightthickness="1", highlightbackground="black")
        self.item3_display.pack(fill="x")
        # self.item4_display = tk.Frame(self.bottom, bg="#F0FFFF", highlightthickness="1", highlightbackground="black")
        # self.item4_display.pack(fill="x")

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

        self.search_button = tk.Button(self.top, text="Search", command=lambda: self.search_items(None),
                                       font=SEARCH_BTN_FONT)
        self.search_button.pack(pady=25, padx=10, side="left")

        self.cart_button = tk.Button(self.top, text="Cart", font=CART_BTN_FONT)
        self.cart_button.pack(pady=25, padx=50, side="left")

        self.no_search = tk.Label(self.bottom, text="No Items Match Your Search", bg="#F0FFFF", font=SEARCH_BAR_FONT)

        # self.button_test = ttk.Button(self.bottom, text="Next", command=lambda: controller.show_page(SecondPage))
        # self.button_test.pack()

        # CATEGORIES
        self.categories = tk.Label(self.middle, text="Categories: ", bg="#F0FFFF", font=SEARCH_BTN_FONT)
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

        # PRODUCT 1
        self.photo1 = tk.PhotoImage(file=ITEMS[0].pic)
        self.thumbnail1 = tk.Label(self.item1_display, image=self.photo1, bg="#F0FFFF")
        self.thumbnail1.image = self.photo1
        self.thumbnail1.pack(side="left")

        self.product_name1 = tk.Label(self.item1_display, text=ITEMS[0].name, bg="#F0FFFF", font=PRODUCT_NAME_FONT)
        self.product_name1.pack(anchor="nw")

        self.product_price1 = tk.Label(self.item1_display, text=ITEMS[0].price, bg="#F0FFFF", font=PRODUCT_NAME_FONT)
        self.product_price1.pack(anchor="ne")

        self.product_brief1 = tk.Label(self.item1_display, text=ITEMS[0].brief, bg="#F0FFFF", font=PRODUCT_NAME_FONT)
        self.product_brief1.pack(anchor="w")

        self.add_to_cart1 = tk.Button(self.item1_display, text="Add to Cart", font=PRODUCT_NAME_FONT)
        self.add_to_cart1.pack(anchor="e")

        self.expand1 = tk.Button(self.item1_display, text="Read More", font=PRODUCT_NAME_FONT,
                                 command=lambda: self.expand(0))
        self.expand1.pack(anchor="sw")

        # PRODUCT 2
        self.photo2 = tk.PhotoImage(file=ITEMS[1].pic)
        self.thumbnail2 = tk.Label(self.item2_display, image=self.photo2, bg="#F0FFFF")
        self.thumbnail2.image = self.photo2
        self.thumbnail2.pack(side="left")

        self.product_name2 = tk.Label(self.item2_display, text=ITEMS[1].name, bg="#F0FFFF", font=PRODUCT_NAME_FONT)
        self.product_name2.pack(anchor="nw")

        self.product_price2 = tk.Label(self.item2_display, text=ITEMS[1].price, bg="#F0FFFF", font=PRODUCT_NAME_FONT)
        self.product_price2.pack(anchor="ne")

        self.product_brief2 = tk.Label(self.item2_display, text=ITEMS[1].brief, bg="#F0FFFF", font=PRODUCT_NAME_FONT)
        self.product_brief2.pack(anchor="w")

        self.add_to_cart2 = tk.Button(self.item2_display, text="Add to Cart", font=PRODUCT_NAME_FONT)
        self.add_to_cart2.pack(anchor="e")

        self.expand2 = tk.Button(self.item2_display, text="Read More", font=PRODUCT_NAME_FONT,
                                 command=lambda: self.expand(1))
        self.expand2.pack(anchor="sw")

        # PRODUCT 3
        self.photo3 = tk.PhotoImage(file=ITEMS[2].pic)
        self.thumbnail3 = tk.Label(self.item3_display, image=self.photo3, bg="#F0FFFF")
        self.thumbnail3.image = self.photo3
        self.thumbnail3.pack(side="left")

        self.product_name3 = tk.Label(self.item3_display, text=ITEMS[2].name, bg="#F0FFFF", font=PRODUCT_NAME_FONT)
        self.product_name3.pack(anchor="nw")

        self.product_price3 = tk.Label(self.item3_display, text=ITEMS[2].price, bg="#F0FFFF", font=PRODUCT_NAME_FONT)
        self.product_price3.pack(anchor="ne")

        self.product_brief3 = tk.Label(self.item3_display, text=ITEMS[2].brief, bg="#F0FFFF", font=PRODUCT_NAME_FONT)
        self.product_brief3.pack(anchor="w")

        self.add_to_cart3 = tk.Button(self.item3_display, text="Add to Cart", font=PRODUCT_NAME_FONT)
        self.add_to_cart3.pack(anchor="e")

        self.expand3 = tk.Button(self.item3_display, text="Read More", font=PRODUCT_NAME_FONT,
                                 command=lambda: self.expand(2))
        self.expand3.pack(anchor="sw")

    def search_items(self, category):
        if category is None:
            words = self.search_bar.get()
        else:
            words = category
        global CURRENT_ITEMS
        CURRENT_ITEMS = []
        for x in ITEMS:
            if x.name.lower() == words.lower() or x.tag.lower() == words.lower():
                CURRENT_ITEMS.append(x)

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

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        title = tk.Label(self, text="JTAB2")
        title.pack(pady=10, padx=10)

        button_test = ttk.Button(self, text="Back", command=lambda: controller.show_page(FrontPage))
        button_test.pack()
