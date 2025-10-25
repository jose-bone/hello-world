#%%
file_name = "history_02.txt"

txt = "My new text file!\n"

with open(file_name, mode="a") as open_file:
    open_file.write(txt)