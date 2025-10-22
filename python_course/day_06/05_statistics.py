def sum_number(a:float, b:float, *args)->float:
    number_values = [a,b] + list(args)
    return sum(number_values)

def average(a:float, b:float, *args)->float:
    return sum_number(a, b, *args) / (len(args)+2)

a = float(input("Insert the A value: "))
b = float(input("Insert the B value: "))
c = float(input("Insert the C value: "))

print("Average:", average(a,b,c))