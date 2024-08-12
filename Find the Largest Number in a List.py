#Find the Largest Number in a List
#Write a function that finds the largest number in a list using a loop. For example, given [4, 7, 1, 8, 3], the output should be 8.
n = int(input("enter the number of elements in list : "))
s = []
v = 0
for i in range(n):
    c = int(input(f"enter {1+i} element :"))
    if c > v:
        v = c
    s.append(c)
print(f"the largest number from this list {s} is : {v}")
