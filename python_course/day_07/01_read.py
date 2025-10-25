#%%
file_name = "history.txt"

with open(file_name) as open_file:
    content = open_file.read()

print(content)

# open_file = open(file_name)
# content = open_file.read()
# open_file.close()