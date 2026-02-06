#string formatting

template = "Dear {}, you are awesome. take this {}$ bag"


a = "john"
a1 = 10000
b = "jack"
b1= 10000
c = "marie"
c2= 300

s1 = template.format(a, a1)
print(s1)

print(f"{a} is awesome this is your prize of {a1}$")
