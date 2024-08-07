# __How to create a class in OOP__

# 1. Adding attributes to a class
class Bird:
	def __init__(self, name, age):
		self.name = name
		self.age = age

# 2.Instantiating objects
# 3. Then, we can create a new Jerry object with a name and age

my_pet = Bird("Jerry", 3)
print(my_pet.name)
print(my_pet.age)
