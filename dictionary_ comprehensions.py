squares = {num: num * 2 for num in range(10)}
print(squares)

scores = {f"player-{num}": num + 1 for num in range(1, 6)}
print(scores)

# create a dictionary from a tuple
scoreboard = [("1", 9999), ("2", 8997), ("3", 7987)]
winners = {key: value for (key, value) in scoreboard}
print(winners)
