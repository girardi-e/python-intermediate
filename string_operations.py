# String has two operations for splitting and joining - split() and join().

my_data = "this,is,comma,separated,data"

# split() returns a list
new_data = my_data.split(",")
print(new_data)

student = "Mary, 16, History"
name, age, subject = student.split(",")
print(name)

# join() returns a string
text = ["Python", "is", "a", "fun", "programming", "language"]
print(" ".join(text))
