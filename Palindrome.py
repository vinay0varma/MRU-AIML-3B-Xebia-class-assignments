#Palindrome Check
#Write a function to check if a given string is a palindrome using a loop. For example, "madam" is a palindrome.
v = input()
if v == v[::-1]:
    print("its palindrome")
else:
    print("its not palindrome")
