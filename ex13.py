# Add features to script from python featureset, similar to ruby require
from sys import argv

# Assign all the variables in order to args
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
