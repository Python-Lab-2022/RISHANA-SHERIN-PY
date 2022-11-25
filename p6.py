list1 = []
list2 = []
n = int(input("enter the elements"))
for i in range(0,n):
    list1.append(int(input()))
print("first list is",list1)
m = int(input("enter the elemnts"))
for i in range(0,m):
    list2.append(int(input()))
print("second list is",list2)
a=len(list1)
b=len(list2)
if a==b:
    print("lists are of same length")
else:
    print("not same")
s=0
for i in list1:
    s+=i
print("Sum of first list is",(s))
t=0
for i in list2:
    t+=i
print("Sum of second list",(t))
if s==t:
    print("sum are equal")
else:
    print("sum is not equal")


num=int(input("enter a number"))
if num in list1 and list2:
    print(num)
else:
    print("no element in common")
common=set(list1).intersection(list2)
print(common,"occur in both")
 

