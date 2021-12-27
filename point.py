class Point:

    # Point constructor (self refers to the current object)
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # instance methods
    def move(self):
        print("move")

    def draw(self):
        print("draw")


# create Point instances
point_one = Point(10, 20)
print(f"The X coordinate is: {point_one.x}.")

point_one.y = 30
print(f"The Y coordinate is: {point_one.y}.")

point_one.draw()
