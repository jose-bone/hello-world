# %%
A = 1
B = 5

print(A)
print(B)

# %%
C = A
A = B
B = C
print(A)
print(B)

# %%
A, B = B, A
print(A)
print(B)

# %%
a, b, *resto = 1, 2, 3, 4, 5, 6, 7, 8, 9
print(a, b, resto)


# %%
def soma(a, *args):
    total = a + sum(args)
    return total


soma(1, 2, 3, 7)

# %%
datas = {"name": "José", "surname": "Boné"}
for i, j in datas.items():
    print(i, j)
