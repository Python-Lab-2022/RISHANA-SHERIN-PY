string = input("Enter the string: ")
string = string[0] + string[1:].replace(string[0],"$")
print(string)
