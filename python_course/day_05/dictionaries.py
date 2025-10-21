#%%

rand_list = [2, 123, "José", ["DS", "DE", "DA"], True]

rand_list[2]

# %%

data_Jose = {"name":"José",
    "lastName":"Boné",
    "sons":False,
    "formation":["IT Support", "Web Dev"],
    "positions":[
        {"name": "Web Dev Jr", "company": "NSD Devil"},
        {"name": "3D Assets", "company": "NSD Devil"},
        {"name": "Mobile Dev", "company": "NSD Devil"},
        {"name": "Backend Dev", "company": "Licungo University"}
    ]
}

#%% 

print(data_Jose)
print(data_Jose["formation"][-1])
print(data_Jose["positions"][-1]["company"])

#%%

data_Jose["marital_status"] = "single"

#%%

print("Keys:", data_Jose.keys())
print("Values:", data_Jose.values())
print("Items:", data_Jose.items())

#%% 

for i in data_Jose:
    print(i, "->", data_Jose[i])

#%%

for (data_keys, data_values)  in data_Jose.items():
    print(data_keys, "->", data_values)