# A module is basically a file with some python code
# We use modules to organize our code into multiple files
# A module should contain all the related functions and classes

# weight conversion lbs -> kg and kg -> lbs
def lbs_to_kg(weight):
    return round(weight * 0.45)


def kg_to_lbs(weight):
    return round(weight / 0.45)
