class ButcherOW:
    def __init__(self, foodname, pounds):
        self.__foodname = foodname #1a
        self.__pounds = pounds #1b
        self.__standardpriceperpound = 0 #1c
        self.__calculated_price = 0 #1d
        self.__pricelist_OW()

    def __pricelist_OW(self): #2
        if self.__foodname == "Dry Cured Iberian Ham":
            self.__standardpriceperpound = 177.80 
        elif self.__foodname == "Wagyu Steak":
            self.__standardpriceperpound = 450.00
        elif self.__foodname == "Matsutake Mushrooms":
            self.__standardpriceperpound = 272.00
        elif self.__foodname == "Kopi Luwak Coffee":
            self.__standardpriceperpound = 306.50
        elif self.__foodname == "Moose Cheese":
            self.__standardpriceperpound = 487.20
        elif self.__foodname == "White Truffles":
            self.__standardpriceperpound = 3600.00
        elif self.__foodname == "Blue Fin Tuna":
            self.__standardpriceperpound = 3603.00
        elif self.__foodname == "Le Bonnotte Potatoes":
            self.__standardpriceperpound = 270.81
        else:
            self.__standardpriceperpound = 0.00

    def calculated_price_OW(self):
        self.__calculated_price = self.__pounds * self.__standardpriceperpound
        return self.__calculated_price
    
item1 = ButcherOW("White Truffles", 5)
print(item1.calculated_price_OW())

