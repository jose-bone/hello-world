text = """
Choose your water to buy
(1) Natural mineral water
(2) Sparkling mineral water 
"""

option = input(text)

bill = 0
if option == "1":
    bill = 1.5

elif option == "2":
    bill = 2.5

if bill == 0:
    print("Insert the fucking correct option, please.")

else:
    print("Your bill came to $", bill)