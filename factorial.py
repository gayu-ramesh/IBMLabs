num=int(input("enter a number"))
fact=1

if num==0:
    print("factorial does not exist")
elif num<0:
    print("enter number greater than 0")
else:
    for i in range(1,num+1):
        fact =fact* i
print(fact)