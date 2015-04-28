# Conditional logic

true = True
false = False
exists = 0

# No need for equality comparison, similar to ruby

if true:
  print(true)

if false:
  print(false)

if not exists:
  print("It exists!")

if exists:
  print("Doesn't exist")



# Concatenating lists
example_list = ['apple', 'banana', 'pear', 'orange']

def print_string(words):
  print(' '.join(words))

print_string(example_list)

print('------------------')

# Swapping variables

one = 1
two = 2

# AKA tuple
one, two = two, one

print(one)
print(two)

print('------------------')

# Getting things from dictionaries

dictionary = { 'James': 5, 'Someone Else': 0 }

def getting_things_from_dictionaries(apple_distribution):
  his_apples = apple_distribution.get('James', 0)
  her_apples = apple_distribution.get('Someone Else', 0)
  print(his_apples, her_apples)

getting_things_from_dictionaries(dictionary)

print('------------------')

name = 'James'

def check_if_name_is_here(name):
  people_i_like = ['James', 'Melissa', 'Richard']

  if name in people_i_like:
    print("Yay")

check_if_name_is_here(name)

print('------------------')

candies = ['Snickers', 'Twix', 'KitKat', 'Mars']

def list_candy_good(listed_things):
  for candy in listed_things:
    print(candy)

list_candy_good(candies)

print('------------------')

