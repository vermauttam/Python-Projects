first_num=float(input("Enter any number: "))
operator=input("Enter any Operator -----> +,-,*,/,**,%,//,sqrt  :")
second_num=float(input("Enter another number: "))

if operator=="+":
    print("Addition is", first_num+second_num)
elif operator=="-":
    print("Subtraction is", first_num-second_num)
elif operator=="*":
    print("Multiplication is", first_num*second_num)
elif operator=="/":
    print("Division is", first_num/second_num)            
elif operator=="%":
    print("Remainder is", first_num%second_num)
elif operator=="//":
    print("Integer is", first_num//second_num)
elif operator=="**":
    print(f"{first_num}**{second_num} is ",first_num**second_num)
else:
    print("Invalid Input")