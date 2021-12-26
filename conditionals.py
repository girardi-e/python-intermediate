# we can include conditionals inside lists comprehension

# only print even numbers in a sequence
even_numbers = ([num * num for num in range(11) if num % 2 == 0])

# string joining with a list comprehension
print(" - ".join([str(even_number) for even_number in even_numbers]))
