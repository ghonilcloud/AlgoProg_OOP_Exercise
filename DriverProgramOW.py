from ClassDefOW import ButcherOW

def listcreator_OW():
    foodlist = list()

    while True:
        num_items = int(input("Enter amount of items: "))
        if num_items >= 1:
            break

    for items in range(num_items):
        name_item = input("Enter the name of the item: )")
        while True:
            num_pounds = eval(input("Enter the amount of pounds: "))
