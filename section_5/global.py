def sum(a,b):
    c = a+b
    global z # tells please modify global z
    z = 0 # will refer to global z and not create a new local variable
    return c
z = 3
print(sum(3,12))
print(z)
