players = ["Max", "Jimmy", "Nina", "Mia"]
scores = [400, 450, 375, 500]

# join two lists with zip function
scoreboard = zip(players, scores)
# zip returns a zip object containing a list of tuples
print(scoreboard)

# loop over a zip object to see its items
for name, score in scoreboard:
    print(f"Player: {name} - Score: {score}")
