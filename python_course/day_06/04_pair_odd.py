def pair_odd(number:int):
    if number % 2 == 0:
        print("Is pair!")
    else:
        print("Is odd!")

number = input("Input a number: ")
number = int(number)

pair_odd(number)