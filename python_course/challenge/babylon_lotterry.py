import random

def get_input():
    while True:
        try:
            user_number = int(input("Enter a number: "))

        except ValueError as err:
            print("Invalid value!")
            continue
            
        if 1 <= user_number <= 15:
            return user_number

        print("Invalid value! The value must be between 1 and 15")

def check_numbers(draw_number, user_number):
    if draw_number == user_number:
        print("Congratulations! You won NOTHING!!")
        return True

    elif user_number > draw_number:
        print("Number too high. Try a low number!")
        return False

    else: 
        print("Number too low. Try a high number!")
        return False

draw_number = random.randint(1,15)

for i in range(3):

    user_number = get_input()
    if check_numbers(draw_number=draw_number, user_number=user_number):
        break

else:
    print("Your attempts are over!!")