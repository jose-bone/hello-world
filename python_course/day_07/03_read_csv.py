#%%
file = "data.csv"

with open(file) as open_file:
    lines = open_file.readlines()

for l in lines:
    print(l)

#%%
datas = dict()

keys = lines[0].strip("\n").split(";")
for c in keys:
    datas[c] = []

#%%
for l in lines[1:]:
    values = l.strip("\n").split(";")
    for i in range(len(values)):
        datas[keys[i]].append(values[i])

datas

#%%
ages = []
for i in datas["age"]:
    ages.append(int(i))

average_age = sum(ages) / len(ages)
average_age