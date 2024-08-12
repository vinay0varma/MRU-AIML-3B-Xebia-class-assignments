Print Multiplication Table
#Write a function that prints the multiplication table for a given number n up to 10.
n = int(input())
for i in range(1,11):
    print(f"{n} * {i} = {n*i}")
