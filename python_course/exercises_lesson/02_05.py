fullName = input("Insert your full name: ")
fullName = fullName.lower()

if "calvo" in fullName.split(" "):
    print("That person is Calvo!")

if "boné" in fullName.split(" "):
    print("That person is Boné!")

if "boné" not in fullName and "calvo" not in fullName:
    print("That person is neither Boné nor Calvo!")