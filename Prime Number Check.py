#Prime Number Check
#Write a function to check if a given number is prime using a loop. For example, is_prime(29) should return True, and is_prime(10) should return False.
def is_prime(n):
    k = 0
    for i in range(2,(n//2)+1):
        if n%i == 0:
            k += 1
    if k ==0 :
        return True
    else:
        return False
print(is_prime(int(input())))
