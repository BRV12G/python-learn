#exception jandling
# while True:
#     try:
#         a = int(input("Enter number 1: "))
#         b = int(input("Enter number 2: "))
#         print(f"The sum is {a + b}")
#     except ValueError:
#         print("Invalid input bad typecasts")
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
#     except Exception as e:
#         print("Unknown error",e)



#rasing an error
# a = int(input("Enter number 1: "))
# b = int(input("Enter number 2: "))
# if b == 0:
#     raise ValueError("Please donot divide by zero")
# print(f"The sum is {a / b}")


#else
# try:
#     a = 345/0
# except Exception as e:
#     print(e)
# else:
#     print("good division no zero")

#finally
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))

try:
    c = a/b
    print(c)
except Exception as e:
    print(e)
finally:
    print("This is always exectued")
