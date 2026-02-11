waterType = input(
    "Select a type of water: (1) Natural Mineral Water / (2) Sparkling Mineral Water \n"
)
if waterType == "1":
    print(
        "Value: 18.00MT",
    )
elif waterType == "2":
    print("Value: 29.99MT")
else:
    print("Insert a valid value!")