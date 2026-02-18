# def sum(a,b):
#     return a+b
# print(sum(324,6,9)) # will throw error: TypeError: sum() takes 2 positional arguments but 3 were given


# def sum(*args):
#     print(args) #will print a tuple (324, 6, 9)
#     total = 0
#     for item in args:
#         total+= item
#     return total
# print(sum(324,6,9))


#kwargs
# kwargs is a dictionary with all the key value pairs which were passed to marks

def marks(**kwargs):
    for item in kwargs.keys():
        print(f" Th marks of {item} is {kwargs[item]}")

marks(shubham=34, vikrant=54, jack=34, Marie=90)

#combing args and kwargs
def func1(*args, **kwargs):
    print(args)
    print(kwargs)

func1(1, 2, 4, 5, jack=34, jill=32, marie=31)
