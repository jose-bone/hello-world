#%%

height_sum = 0
entries_qtty = 4

for i in range(entries_qtty):
    height = input("Insert the height: ")
    height = float(height)
    height_sum += height

print("The height sum:", height_sum)