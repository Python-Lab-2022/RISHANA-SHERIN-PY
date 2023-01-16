def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
print("Enter a number")
n=int(input())
print("The factorial of",n, "is",fact(n))
