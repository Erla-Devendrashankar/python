# to print series of 1,a,@
a=int(input("enter the number:"))
for i in range(1,a+1):
    if i%3==0:
        print("1",end=" ")
    elif i%3==1:
        print("a",end=" ")
    elif i%3==2:
        print("@",end=" ")