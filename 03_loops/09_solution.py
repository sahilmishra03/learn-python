items = ["apple", "banana", "orange", "apple", "mango"]
flag = True
for i in items:
    if items.count(i)>1:
        flag=False
        break
if(flag):
    print("No Duplicate")
else:
    print("Duplicate")