def main():
    a = int(input("Enter digits = "))
    print("addition of digits is =", addition(a))
def addition(x):
    sum = 0
    while  x > 0:
        sum += x % 10
        x = x // 10
    return sum

main()
