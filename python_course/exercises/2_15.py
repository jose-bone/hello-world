#%%

number_list = [1,2,3,3,2,1,1,1,1,5,6,7,6,5,4]

number = input("Insert one number: ")
number = int(number)

count = 0
for i in number_list:
    if i == number:
        count += 1

print("The number", number, "appear", count, "time(s)")