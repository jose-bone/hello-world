iceCreamType = input(
    "Insert the type of ice cream: [Cone (12MT), Tub (29.99MT), Basket (47.99MT)]"
)
iceCreamType = iceCreamType.lower()

flavour = input("Choose your flavour: [Strawberry / Cream / Chocolate]")
flavour = flavour.lower()

iceCreamTopping = input(
    "Choose the topping: [Caramel (18MT), Strawberry (18MT), Chocolate (18MT), No topping (0.00)]"
)
iceCreamTopping = iceCreamTopping.lower()

iceCreamValue = 0
if iceCreamType == "cone":
    iceCreamValue += 12
elif iceCreamType == "tub":
    iceCreamValue += 29.99
elif iceCreamType == "basket":
    iceCreamValue += 47.99

if iceCreamTopping in ["caramel", "strawberry", "chocolate"]:
    iceCreamValue += 18

txt = f"Your ice cream {iceCreamType} with topping of {flavour} cost {iceCreamValue:.2f}MT"
print(txt)