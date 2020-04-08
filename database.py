import random


class Database:

    def __init__(self, name, price, brief, full, pic, tag):
        self.name = name
        self.price = price
        self.brief = brief
        self.full = full
        self.pic = pic
        self.tag = tag
        self.in_cart = 0


def populate_items(list_of_items):
    pencil = Database("Pencil", .99, "It writes stuff.",
                      "You may use this pencil to write.\nYou can write many things.\nWrite whatever you want.",
                      "x.gif", "school")
    list_of_items.append(pencil) # 1

    pen = Database("Pen", .99, "It writes stuff.",
                   "You may use this peen to write.\nYou can write many things.\nWrite whatever you want.",
                   "test3.png", "school")
    list_of_items.append(pen) # 2

    paper = Database("Paper", 1.99, "You can write on it.",
                     "You may write stuff on this paper.\nYou can write many things on it.\nWrite whatever you want.",
                     "test2.png", "school")
    list_of_items.append(paper) # 3

    bike = Database("Bike", 10.99, "You can ride it.",
                        "You can ride on this bicycle.\nYou can go to many places on it.\nGo wherever you want.",
                        "Test.png", "transport")
    list_of_items.append(bike) # 4

    skateboard = Database("Skateboard", 4.99, "You can ride it.",
                    "You can ride on this skateboard.\nYou can go to many places on it.\nGo wherever you want.",
                    "Test.png", "transport")
    list_of_items.append(skateboard) # 5

    monopoly = Database("Monopoly", 3.99, "You can play it.",
                          "You can play this game.\nYou can play it with many people.\nPlay whenever you want.",
                          "Test.png", "games")
    list_of_items.append(monopoly) # 6

    hammer = Database("Hammer", 2.99, "You can build things.",
                        "You can swing this hammer.\nYou can hit many nails.\nBuild whatever you want.",
                        "Test.png", "tools")
    list_of_items.append(hammer)  # 7

    nails = Database("Nails", 1.99, "You can build things.",
                      "You can nail things together.\nYou can use many nails.\nBuild whatever you want.",
                      "Test.png", "tools")
    list_of_items.append(nails)  # 8

    saw = Database("Saw", 3.99, "You can saw things.",
                     "You can saw things into pieces.\nYou can use saw many things.\nSaw whatever you want.",
                     "Test.png", "tools")
    list_of_items.append(saw)  # 9

    apple = Database("Apple", .99, "You can eat this.",
                     "You can eat this apple.\nYou can use this in many recipes.\nEat it whenever you want.",
                     "Test.png", "food")
    list_of_items.append(apple)  # 10

    orange = Database("Orange", .99, "You can eat this.",
                     "You can eat this orange.\nYou can use this in many recipes.\nEat it whenever you want.",
                     "Test.png", "food")
    list_of_items.append(orange)  # 11

    watermelon = Database("Watermelon", 1.99, "You can eat this.",
                      "You can eat this watermelon.\nYou can use this in many recipes.\nEat it whenever you want.",
                      "Test.png", "food")
    list_of_items.append(watermelon)  # 12

    shirt = Database("Shirt", 1.99, "You can wear this.",
                          "You can wear this shirt.\nYou can wear this on many days.\nWear it wherever you want.",
                          "Test.png", "clothes")
    list_of_items.append(shirt)  # 13

    pants = Database("Pants", 2.99, "You can wear these.",
                     "You can wear these pants.\nYou can wear these on many days.\nWear these wherever you want.",
                     "Test.png", "clothes")
    list_of_items.append(pants)  # 14

    keyboard = Database("Keyboard", 9.99, "You can type stuff.",
                          "You can type on this keyboard.\nYou can type many things.\nType whatever you want.",
                          "Test.png", "technology")
    list_of_items.append(keyboard)  # 15


def randomize_items(items):
    for x in range(0, 15):
        num = random.randint(0, 14)
        temp = items[0]
        items[0] = items[num]
        items[num] = temp
    return items
