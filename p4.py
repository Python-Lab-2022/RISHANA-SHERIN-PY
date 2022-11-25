list=[]
list1=[]
n=int(input("enter the number"))
for i in range(0,n):
    list.append(int(input()))
    print("list is:",list)
for i in list:
    if i>100:
        list1.append('over')
    else:
        list1.append(i)
print("result list is",list1)
