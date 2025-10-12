#%%
name = "José Boné"

for letter in name:
    print(letter)

#%%

number = 4
max_number = 50

for i in range(1, max_number + 1):
    print(number, "X", i, "=", number * i)

#%%

for i in range(4, 101):
    if i % 4 == 0:
        print(i)