from pages import *


class JtabCommerce(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        tk.Tk.wm_title(self, "JTAB Inc.")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.pages = {}

        for x in (FrontPage, SecondPage, ThirdPage, FourthPage, FifthPage):
            page = x(container, self)
            self.pages[x] = page
            page.grid(row=0, column=0, sticky="nsew")

        self.show_page(FrontPage)

    def show_page(self, controller):
        page = self.pages[controller]
        page.tkraise()


# server = smtplib.SMTP('smtp.gmail.com', 587)  # Connect to the server
# server.starttls()  # Use TLS
# server.login("jakobpatino@gmail.com", "b********")  # Login to the email server
# server.sendmail("jakobpatino@gmail.com", "jakobpatino@gmail.com", "Test")  # Send the email
# server.quit()  # Logout of the email server
run = JtabCommerce()
run.geometry("900x700+300+50")
run.mainloop()
