def calculator():
  a = int(input("enter first num = "))
  b = int(input("enter secound num = "))
  ch = (input("enter operation = "))
  if (ch == "+" ) :
    print("addition of two numbers = ", a+b)

  elif(ch == "-"):
    print("substraction of two numbers = ", a-b)

  elif(ch == "/" ):
    print("division of two numbers = ", a/b)

  elif(ch == "*"):
    print("multiplication of two numbers = ", a*b)

  else:
    print("invalid input please enter valid input")

calculator()
