items = "orange carnation beer noodles lasagne"

chooseItem = input("Choose an item: ").lower()

if chooseItem in items:
    print("Your chosen item is available!")
else:
    print("Please select a valid item!")