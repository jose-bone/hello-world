waterType = input(
    "Select a type of water: (1) Natural Mineral Water / (2) Sparkling Mineral Water \n"
)

waterQuantity = int(input("How many bottles?\n"))

if waterType == "1":
    waterValue = 18 * waterQuantity
    print("Total: ", waterValue, "MT")
elif waterType == "2":
    waterValue = 29 * waterQuantity
    print("Total: ", waterValue, "MT")
else:
    print("Insert valid data!")