fruit = input("Insert the fruit name:")

fruits = {
    "Apple": "R$1,50",
    "Banana": "R$2,75",
    "Grape": "R$1,90",
    "Pear": "R$1,25",
    "Orange": "R$0,65",
    "Lemon": "R$1,25",
    "Guava": "R$2,15",
    "Pineapple": "R$3,20",
    "Jackfruit": "R$5,80",
}

if fruit in fruits:
    print(fruits[fruit])
else:
    print("Insert a valid value!!")