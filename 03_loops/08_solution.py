num = 4
flag = True
for i in range(2,num):
    if num%i==0:
        print("Not Prime")
        flag=False
if flag:
    print("Prime")