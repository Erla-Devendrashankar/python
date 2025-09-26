a=int(input("enter the number:"))
for i in range(1,a):
    if a%2!=0:
        if i==a-2:
            print(i,end=".")
        elif i%2!=0:
            print(i,end=",")
    else:
        if i==a-1:
            print(i,end=".")
        elif i%2!=0:
            print(i,end=",")