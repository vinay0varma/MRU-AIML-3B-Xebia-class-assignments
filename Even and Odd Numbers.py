Even and Odd Numbers
#Write a function that takes a list of integers and returns two lists: one containing all the even numbers and the other containing all the odd numbers.
print("enter the integers")
even_list = []
odd_list = []
b = True
while b:
    c = input()
    if c.isdigit():
        if int(c)%2 == 0:
            even_list.append(int(c))
        else:
            odd_list.append(int(c))
    else:
        print("you not entered the number ")
        break
print("even numbers list : ",even_list )
print("odd  numbers list : ",odd_list)
