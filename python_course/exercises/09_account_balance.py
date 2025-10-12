total_balance = 0
while True:
    balance = input("Input your balance: ")
    if balance == "":
        break
    
    total_balance += float(balance)

print("The total balance:", total_balance)