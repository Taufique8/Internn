a = int(input("Enter Your Number: "))
b = int(input("Enter Your Number: "))
op = input("Enter Your Operater: ")
if(op=='+'):
    print("Addition: ",a+b)
elif(op=='-'):
    print("Substraction: ",a-b)
elif(op=='*'):
    print("Multiplaction: ",a*b)
elif(op=='/'):
    print("Division: ",a/b)
else:
    print("Enter a Valid Operator")
    
