#Sum of Even and Odd Numbers in a List
#Write a function that takes a list of integers and returns a tuple with the sum of even numbers and the sum of odd numbers. For example, for the list [1, 2, 3, 4, 5, 6], the output should be (12, 9).
def get_sum(lis):
    v = []
    v.append(sum(lis[0]))
    v.append(sum(lis[1]))
    return tuple(v)
    
    
n = int(input("enter any variable to stop inserting : "))
s = [[],[]]
while True:
    v = input("insert number: ")
    if v.isdigit():
        v = int(v)
        if v%2 == 0:
            s[1].append(v)
        else:
            s[0].append(v)
    else:
        print("inserting ended")
        break
s = get_sum(s)
print(s)
