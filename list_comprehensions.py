students = ["Jessica", "Maria", "Josh", "Carmen"]

print([student.upper() for student in students])

# return a list of numbers from 0 to 10
print([num * 2 for num in range(11)])

# return a list of tuples
name_length = [
    (f"student: {student}, length: {len(student)}") for student in students
]
print(name_length)

# list comprehension with string format
print("\n".join([f"The student's name is {student}" for student in students]))
