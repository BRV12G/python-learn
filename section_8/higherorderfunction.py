# numbers = [1,2,3,4,5]
# def  square(x):
#     return x*x

# new = list(map (square, numbers))
# print(new) #<map object at 0x000001AFA01F4580> without typecasting to list
# print(new)




#filter
# def is_greater_than_9(x):
#     if x>9:
#         return True
#     else:
#         return False
# a = [3,67,4,56,9,2345,78,0,45,6,89,8]
# new = list(filter(is_greater_than_9, a))
# # print(new) #<filter object at 0x000001ABE98145B0> without typecasting to list
# print(new)


#reduce
from functools import reduce

numbers = [1,2,3,4,5,6]
# [3, 3, 4, 5, 6]
# [6, 4, 5, 6]
# [10, 5, 6]
# [15, 6]
# [21]

def sum(a,b):
    return a+b
c = reduce(sum, numbers)
print(c)
