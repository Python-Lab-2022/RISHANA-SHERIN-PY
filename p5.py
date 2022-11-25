list=[]
n=int(input("Enter the number of elements"))
for i in range(0,n):
    list.append(str(input()))
print(list)
count=0
for i in list:
    for i in i:
        if i=='a':
            count=count+1
print("count=",count)
