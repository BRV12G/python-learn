# num = int(input("enter a number"))
# if(num<0):
#     print("number is negative")
# elif(num>0):
#     print("number is positive")
# else:
#     print("number is zero")

# #2
# age = int(input("enter your age"))
# if(age>=18):
#     print("you can vote")
# else:
#     print("you cannot vote")


# #3
# num = int(input("enter a number"))
# if(num%2==0):
#     print("number is even")
# else:
#     print("number is odd")



# #21
# num = int(input("enter a number"))
# match num:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("invalid input")

# #22
# num1 = int(input("enter first number"))
# num2 = int(input("enter second number"))
# op = str(input("enter operator"))

# match op:
#     case "+":
#         print(num1+num2)
#     case "-":
#         print(num1 - num2)
#     case "*":
#         print(num1 * num2)
#     case "/":
#         print(num1 / num2)
#     case _:
#         print("invalid operator")

#31
# for i in range(1,11):
#     print(i)

# #32
# num = int(input("enter a number"))

# for i in range(1, 11):
#     print( num ," X ", i, " = ", num*i)

# sum=0
# for i in range(1, 101):
#     sum=sum+i
# print(sum)

# for i in range(1,5):
#     print("*"*i)



#while loops
i=1
while i<=10:
    print(i)
    i+=1


pass_enter = input("enter password")
passreal = "geelo"
while pass_enter != passreal:
    pass_enter = input("try again, enter password")
print("password accepted")



