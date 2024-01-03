number1=int(input("enter the number1:"))
number2=int(input("enter the number2:"))
option=int(input("Enter an option:"))
if(option==1):
    sum=number1+number2
    print("sum=",sum)
elif(option==2):
    if(number1>number2):
        subtract=number1-number2
        print("subtract=",subtract)
    else:
        subtract=number2-number1
        print("subtract=",subtract)

elif(option==3):
    Multiplicate=number1*number2
    print("Multiplicate=",Multiplicate)
elif(option==4 ):
    if(number1>number2 & number2!=0):
        Divide=number1/number2
        print("Divide=",Divide)
    else:
        print("Invalid")
else:
    print("None")
