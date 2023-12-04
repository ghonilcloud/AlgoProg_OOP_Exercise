from ClassDefOW import ButcherOW

def listcreator_OW():
    foodlist = []

    while True:
        num_items = int(input("Enter amount of items: "))
        if num_items >= 1:
            break

    itemadd = 0
    for items in range(num_items):
        itemadd += 1
        print(f'Add Item #{itemadd}')

        name_item = input("Enter the name of the item: ")
        while True:
            num_pounds = eval(input("Enter the amount of pounds: "))
            if num_pounds >= 1:
                break
        foodlist.append(ButcherOW(name_item, num_pounds))

    return foodlist

def reveal_foodlist_OW(list):
    for item in list:
            print(f'Item: {item.getName_OW()}')
            print(f'Amount Ordered: {item.getAmount_OW()}')
            print(f'Price Per Pound: {item.getStandardpriceperpound_OW()}')
            print(f'Price of order: {item.getCalculatedPrice_OW()}')
            print(f'\n')

def calculate_total_OW(list):
    total = []
    for item in list:
        total.append(item.pricelisttotal_OW())
    return sum(total)

def main_OW():
    list = listcreator_OW()
    reveal_foodlist_OW(list)
    return calculate_total_OW(list)

main_OW()
