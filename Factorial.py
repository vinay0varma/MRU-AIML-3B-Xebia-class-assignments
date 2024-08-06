def factorial():
    #instalizatoin
    a = int(input("Enter a number = "))
    i = a
    fact = 1
    #loop
    while i > 0 :
        fact = fact * a
        i -= 1
    print("factorial of",  a, "is =", fact)

factorial()
