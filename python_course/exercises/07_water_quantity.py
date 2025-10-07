text = """
Choose your water to buy
(1) Natural mineral water - 1.5
(2) Sparkling mineral water - 2.5 
"""

option = input(text)

item_value = 0
if option == "1":
    item_value = 1.5
elif option == "2":
    item_value = 2.5

if item_value == 0:
    print("Insert the fucking correct option, please.")

else:
    quantity = input("How many bottles? ")
    quantity = int(quantity)
    total_value = item_value * quantity
    print("Your bill came to: $", total_value)