
def average(a,b,c):
    d = (a+b+c)/3.0
    print(d)

average(3,5,1)
def average2(a,b,c):
    d = (a+b+c)/3.0
    return d
o1=average2(3,7,1)

print(o1)


#arguments
def add(a,b):
    return(a+b)
c = add(2,1)
print(c)


def add(a,b,plus=0):
    return(a+b+plus)
c = add(2,1)
d = add(2,1,2)
print(c)
print(d)

