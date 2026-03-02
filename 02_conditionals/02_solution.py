age = int(input("Enter ur age -> "))
day = input("Enter ur day -> ")

price = 0;

if(age>=18):
    price=12
else:
    price=8

if(day=="Wednesday"):
    price=price-2

print(f"Final Price is -> {price}")