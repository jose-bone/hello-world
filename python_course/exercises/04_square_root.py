number = input("Insert a INT number to calculate the square root: ")
number = int(number)

squareRoot = number ** (1/2) # number ** 0.5
squareRoot = round(squareRoot, 4)

print("The square root of", number, "is:", squareRoot)