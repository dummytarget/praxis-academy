class Person:
  def __init__(self, name, age):
      self.name = name
      self.age = age

  def say_hi(self):
      print('Hello, my name is', self.name, '. My age is', self.age)

p = Person('Kadek', 12)
p.say_hi()

# Hello, my name is, Kadek. My age is 12