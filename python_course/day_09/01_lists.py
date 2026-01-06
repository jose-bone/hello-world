# %%
x = []
for i in range(1, 101):
    x.append(i)

x

# %%
y = [i for i in range(1, 101)]
y


# %%
def is_pair(x):
    return x % 2 == 0


z = [is_pair(i) for i in range(1, 101)]
z

#%%
w =[i for i in range(1,101) if is_pair(i)]
w