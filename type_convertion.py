# string -> integer
age = "5"
print(7 + int(age))

# integer -> string
number = 11
print("My favorite number is " + str(number))

# float -> int
grade = 3.7
print(int(grade))

# int -> float
gpa = 4
print(float(gpa))

# string -> list
greeting = "Hello there!"
print(list(greeting))
print(" ".join(list(greeting)))

# list -> set (eliminate duplicates)
names = ["Bob", "Jeff", "Peter", "Susan", "Bob", "Mike"]
print(set(names))
# return a sorted list
print(sorted(set(names)))
