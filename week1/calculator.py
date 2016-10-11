firstNumb = int(input("First number: "))
secondNumb = int(input("Second number: "))
oper = input("Choose operation: ")

if (oper == "+"):
    print(firstNumb + secondNumb)
elif (oper == "-"):
    print(firstNumb - secondNumb)
elif (oper == "*"):
    print(firstNumb * secondNumb)
elif (oper == "/"):
    print(firstNumb / secondNumb)
else:
    print("We dont support that operation.")

