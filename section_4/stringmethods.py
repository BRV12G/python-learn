name = "bhairavi"
a = len(name)
print(a)
print(name.upper(),name)
print(name.lower())
print(name.capitalize())


text = "   hello world   "
print(text.strip())
print(text.lstrip())
print(text.rstrip())


text = "python is fun and fun"
print(text.find("is"))
print(text.replace("fun","awesome"))


text = " Apples, Bananas, Pineapples, Mangoes"
print(text.split(","))
print(",".join([' Apples', ' Bananas', ' Pineapples', ' Mangoes']))

text = "python123"
print(text.isalpha())
print(text.isalnum())
print(text.isdigit())
print(text.isspace())
