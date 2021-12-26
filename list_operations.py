squares = [num * num for num in range(6)]

squares_sum = sum(squares)
print(f"The total sum is : {squares_sum}")

squares_max = max(squares)
print(f"The biggest number is: {squares_max}")

squares_min = min(squares)
print(f"The lowest number is: {squares_min}")

squares_sorted = sorted(squares, reverse=True)
print(squares_sorted)

lottery_numbers_string = "15, 24, 26, 30, 42, 59, 18"

# convert string into list
lotto_numbers = lottery_numbers_string.split(",")

# convert strings into integers
print(max([int(num) for num in lotto_numbers]))
