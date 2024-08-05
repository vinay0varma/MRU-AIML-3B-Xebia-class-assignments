def fibonacci():
    # Intailization
    t1 = 0
    t2 = 1
    nextterm = 0
    n = int(input("enter number of values = "))

    # loop for finding fibonacci series upto n
    for i in range (n):
        print(nextterm)
        t1 = t2
        t2 = nextterm
        nextterm = t1 + t2

fibonacci()
