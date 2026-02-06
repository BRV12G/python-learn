# name = "Bhairavi"
# print(name[0])
# print(name[-1])
# print(len(name))
# print("Hello", "World")


# text = "Python Programming"
# print(text[0:6])
# print(text[-6:])
# print(text[::2])
# print(text[::-1])


# text = " i love python programming "
# print(text.strip())
# print(text.title())
# print(text.count("o"))
# print(text.isalnum())

# name = "John"
# age = 25
# print(f"My name is {name} and I am {age} years old.")


# sentence = "Coding in Python is fun"
# print(sentence.replace("fun", "awesome"))
# print(sentence.find("Python"))
# print(sentence.upper())

sentence = "Coding in Python is fun"
sum = 0
vowels = ["a", "e", "i", "o", "u"]
for char in sentence:
    print(char)
    if(char in vowels):
        sum+=1
print(f"There are {sum} vowels in the sentence.")


string1 = "madam"
if(string1 == string1[::-1]):
    print("palindrome")
else:
    print("no palindrome")

