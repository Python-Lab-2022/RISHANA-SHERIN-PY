d = {}
s = input("Enter a string:")
for i in s:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)
