x=[]
n=int(input("enter the list of items:"))
for i in range(n):
    x.append(int(input()))
print("The list of items:-",x)
s=0
for i in x:
    s+=i
print("Sum of all items in the list:",s)

