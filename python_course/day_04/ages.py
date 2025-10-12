#%%

ages = []

while True:
    age = input("Insert the age: ")

    if age == "":
        break

    ages.append(int(age))

average = sum(ages) / len(ages)
minimum = min(ages)
maximum = max(ages)
qtty = len(ages)

print("AVERAGE:", average)
print("MINIMUM:", minimum)
print("MAXIMUM:", maximum)
print("QUANTITY:", qtty)