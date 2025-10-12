height_sum = 0
entries_qtty = 4

while entries_qtty > 0:
    height = input("Insert the height: ")
    height = float(height)
    height_sum += height
    entries_qtty -= 1

print("The height sum:", height_sum)