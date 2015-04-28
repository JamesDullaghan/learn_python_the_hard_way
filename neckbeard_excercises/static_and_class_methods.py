class Item(object):

  rock = False
  paper = True
  scissor = False

  def __init__(self, number):
    self.number = number

  @staticmethod
  def static_method():
    print("This is a static method")

  @classmethod
  def class_method(cls):
    print("This is a class method that belongs to %s and the paper is" % cls, cls.paper)

# They can both be invoked from instances or the class

i = Item(8)
i.static_method()
i.class_method()

Item.static_method()
Item.class_method()

# Static methods - No information about class or instance it's called upon
#   Simple methods to compute something and return a result

print('------------------')

from random import choice

COLORS = ['Brown', 'Black', 'Golden', 'Green', 'Blue', 'Red']

class Animal(object):
  def __init__(self, color):
    self.color = color

  @classmethod
  def make_baby(cls):
    color = choice(COLORS)
    return cls(color)

  @staticmethod
  def speak():
    print("Roar!")

class Dog(Animal):
  @staticmethod
  def speak():
    print("Bark!")

  # Superclass make_baby method is called
  #  Passing the dog class to super
  #
  @classmethod
  def make_baby(cls):
    print("Making baby dog!")
    return super(Dog, cls).make_baby()

class Cat(Animal):
  pass

print('------------------')

dog = Dog('Brown')
pup = dog.make_baby()
pup
print(pup.color)

print('------------------')

Dog.speak()
pup.speak()
dog.speak()
Animal.speak()

print('------------------')

cat = Cat('Red')
print(cat.color)
kitty = cat.make_baby()
print(kitty.color)
kitty.speak()
