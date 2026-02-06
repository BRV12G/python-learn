marks = [54,45,67,89,90]
mixed = [43, "hello",False,4.2]
print(marks[0])
print(marks[2:4])
extra_marks = [56,78,90,23,45]

print(marks)
marks.append(63)
print(marks)
marks.pop()
print(marks)
marks.clear()
print(marks)
marks.extend(extra_marks)
new_marks = marks.copy()
print(new_marks)

print(marks.count(45))

marks.remove()
