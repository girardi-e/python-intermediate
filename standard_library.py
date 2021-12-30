import os
import sys

# the os module allows you to get a file listing for the folder 
# your new file is 
my_folder = os.getcwd()
print(f"Here are the files in {my_folder}: ")

with os.scandir(my_folder) as folder:
    for entry in folder:
        print(f" - {entry.name}")

# sys is another commonly useful library, giving you access to some variables
# and functions used or maintained by the Python interpreter.
arguments = sys.argv
print("We have received the following arguments:")

for arg in arguments:
    print(f" - {arg}")

print(f"We're running on a {sys.platform} machine")
