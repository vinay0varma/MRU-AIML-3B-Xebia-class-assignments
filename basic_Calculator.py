# Basic Calculator
def calculator():
  a = int(input("enter first num = "))
  b = int(input("enter secound num = "))
  isExit = False
  #loop
  while(isExit != True):

    print("---Menu---\nEnter below option \n 1. Addition = + \n 2. Substraction = - \n 3. Division = / \n 4. Multiplication = * 5. Exit = & ")
    ch = (input("enter operation = "))
    # addition
    if (ch == "+"):
      print("addition of two numbers = ", a+b)

    # substraction
    elif(ch == "-"):
     print("substraction of two numbers = ", a-b)

    #division
    elif(ch == "/" ):
      print("division of two numbers = ", a/b)

    #multiplication
    elif(ch == "*"):
      print("multiplication of two numbers = ", a*b)

    #exit loop
    elif(ch == "&"):
      isExit == True
      break

    else:
      print("invalid input please enter valid input")


calculator()
