class Person:

    number_of_people = 0

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        Person.number_of_people += 1

    def introduce_self(self):
        print(f"Hi! I'm {self.first_name} {self.last_name}.")

    def greet(self):
        print("Hello there! How's it going?")

    def hurry(self):
        print("Sorry, but I have to hurry. Catch you later.")

    @classmethod
    def get_number_of_people(cls):
        return f"Total number of people: {cls.number_of_people}"


jenny = Person("Jenny", "Smith", 25)
jenny.introduce_self()

bob = Person("Bob", "Brown", 33)
print(f"First name: {bob.first_name}")

number_of_people = Person.get_number_of_people()
print(number_of_people)
