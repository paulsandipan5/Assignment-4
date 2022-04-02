# Write a Python program to square the elements of a list using map() function.

list1 = []
n = int(input("Enter the numbers of elements:"))
for i in range(n):
    list1.append(int(input()))
print(list1)

def square_num(num):
    return num*num
print("Square elements of the list:",list(map(square_num ,list1)))
    