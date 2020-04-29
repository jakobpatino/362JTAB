from pages import *


class JtabCommerce(tk.Tk):
    # JTAB Commerce Class
    # Date: 4/4/20
    # Programmer: Jakob
    # Description: manages the whole program window and switches between pages
    # Data Structures: dictionary

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)  # initialize tk

        tk.Tk.wm_title(self, "JTAB Inc.")      # change title in top of window

        # format the program's window
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.pages = {}  # a dictionary that will contain all the pages of the program

        # add all pages to dictionary
        for x in (FrontPage, SecondPage, ThirdPage, FourthPage, FifthPage):
            page = x(container, self)
            self.pages[x] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page(FrontPage)  # displays the front page on program startup

    def show_page(self, controller):
        # Show Page
        # Date: 4/4/20
        # Programmer: Jakob
        # Description: switches between individual pages in the dictionary and brings them to the front
        # Data Structures: dictionary
        page = self.pages[controller]
        page.tkraise()  # displays the page in front


run = JtabCommerce()            # initialize the window
run.geometry("900x700+300+50")  # format the size and screen location of the window
run.mainloop()                  # run the program loop
