# Write a Python program to triple all numbers of a given list of integers. Use Python map

l = []
n = int(input("Enter the numbers of elements:"))
for i in range(n):
    l.append(int(input()))
print(l)

def triple_num(num):
    return 3*num
print(list(map(triple_num ,l)))