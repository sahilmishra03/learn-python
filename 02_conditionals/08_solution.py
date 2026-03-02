password = input("Enter password for check")
password=password.strip()
if(len(password)<6):
    print("Weak")
elif(len(password)>6 and len(password)<=15):
    print("Medium")
else:
    print("Strong")