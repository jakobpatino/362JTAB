import random


class Database:
    # Database Class
    # Date: 4/5/20
    # Programmer:
    # Description: keeps track of all data for an item that will be in the database
    # Data Structures: N/A

    def __init__(self, name, price, brief, full, pic, tag):
        self.name = name    # name of product
        self.price = price  # price of product
        self.brief = brief  # brief description of product
        self.full = full    # full description of product
        self.pic = pic      # picture of product
        self.tag = tag      # tag to search for item
        self.in_cart = 0    # number of this item in cart


def populate_items(list_of_items):
    # Populate Items Module
    # Date: 4/5/20
    # Programmer:
    # Description: creates all items in the database and adds them to the list
    # Data Structures: list

    pencil = Database("Pencil", .99, "It writes stuff.",
                      "You may use this pencil to write.\nYou can write many things.\nWrite whatever you want.",
                      "images/pencil.png", "school")
    list_of_items.append(pencil)  # 1

    pen = Database("Pen", .99, "It writes stuff.",
                   "You may use this peen to write.\nYou can write many things.\nWrite whatever you want.",
                   "images/pen.png", "school")
    list_of_items.append(pen)  # 2

    paper = Database("Paper", 1.99, "You can write on it.",
                     "You may write stuff on this paper.\nYou can write many things on it.\nWrite whatever you want.",
                     "images/paper.png", "school")
    list_of_items.append(paper)  # 3

    bike = Database("Bike", 10.99, "You can ride it.",
                    "You can ride on this bicycle.\nYou can go to many places on it.\nGo wherever you want.",
                    "images/bike.png", "transport")
    list_of_items.append(bike)  # 4

    skateboard = Database("Skateboard", 4.99, "You can ride it.",
                          "You can ride on this skateboard.\nYou can go to many places on it.\nGo wherever you want.",
                          "images/skateboard.png", "transport")
    list_of_items.append(skateboard)  # 5

    monopoly = Database("Monopoly", 3.99, "You can play it.",
                        "You can play this game.\nYou can play it with many people.\nPlay whenever you want.",
                        "images/monopoly.png", "games")
    list_of_items.append(monopoly)  # 6

    hammer = Database("Hammer", 2.99, "You can build things.",
                      "You can swing this hammer.\nYou can hit many nails.\nBuild whatever you want.",
                      "images/hammer.png", "tools")
    list_of_items.append(hammer)  # 7

    nails = Database("Nails", 1.99, "You can build things.",
                     "You can nail things together.\nYou can use many nails.\nBuild whatever you want.",
                     "images/nail.png", "tools")
    list_of_items.append(nails)  # 8

    saw = Database("Saw", 3.99, "You can saw things.",
                   "You can saw things into pieces.\nYou can use saw many things.\nSaw whatever you want.",
                   "images/saw.png", "tools")
    list_of_items.append(saw)  # 9

    apple = Database("Apple", .99, "You can eat this.",
                     "You can eat this apple.\nYou can use this in many recipes.\nEat it whenever you want.",
                     "images/apple.png", "food")
    list_of_items.append(apple)  # 10

    orange = Database("Orange", .99, "You can eat this.",
                      "You can eat this orange.\nYou can use this in many recipes.\nEat it whenever you want.",
                      "images/orange.png", "food")
    list_of_items.append(orange)  # 11

    watermelon = Database("Watermelon", 1.99, "You can eat this.",
                          "You can eat this watermelon.\nYou can use this in many recipes.\nEat it whenever you want.",
                          "images/watermelon.png", "food")
    list_of_items.append(watermelon)  # 12

    shirt = Database("Shirt", 1.99, "You can wear this.",
                     "You can wear this shirt.\nYou can wear this on many days.\nWear it wherever you want.",
                     "images/shirt.png", "clothes")
    list_of_items.append(shirt)  # 13

    pants = Database("Pants", 2.99, "You can wear these.",
                     "You can wear these pants.\nYou can wear these on many days.\nWear these wherever you want.",
                     "images/pants.png", "clothes")
    list_of_items.append(pants)  # 14

    keyboard = Database("Keyboard", 9.99, "You can type stuff.",
                        "You can type on this keyboard.\nYou can type many things.\nType whatever you want.",
                        "images/keyboard.png", "technology")
    list_of_items.append(keyboard)  # 15


def randomize_items(items):
    # Randomize Items
    # Date: 4/5/20
    # Programmer:
    # Description: shuffle database items in the list
    # Data Structures: list

    for x in range(0, 15):
        num = random.randint(0, 14)
        temp = items[0]
        items[0] = items[num]
        items[num] = temp
    return items
