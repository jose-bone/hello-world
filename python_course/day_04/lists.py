#%% 

ages = [30, 28, 42, 45, 50, 39, 18]
print(ages)

#%%

developer = ["José", "Boné", 30, "Single"]
print(developer)

#%%
type(developer)

#%%

# First name
print(developer[0])

# Last name
print(developer[1])

# Marital state
print(developer[3])

#%%

ages = [30, 28, 42, 45, 50, 39, 18, 41, 23]
print("Ages sum:", sum(ages))
print("Ages quantity:", len(ages))
print("Average ages:", sum(ages) / len(ages))
print("Min age:", min(ages))
print("Max age:", max(ages))

#%%

developer = ["José", 
             "Boné", 
             30, 
             "Single", 
             ["Intern", "Student", "Volunteer", "3D Asset", "Web Dev"], 
             ["Vodafone", "Nokia", "XIAOMI"]]

print(developer[4][2])

mobiles = developer[5]
first_mobile = mobiles[1]
print(first_mobile)

#%%

list_size = len(developer)
list_position = list_size - 1
developer[list_position][0]

#%%

developer[-1][-1]

#%%

developer[0:4]

#%%

developer[4][3:5]

#%%

developer[4][-2:]

#%%

skills = developer[4]
skills[::-1]