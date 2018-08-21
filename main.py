# parent class
class Mammal(object):
# initialize here
  def __init__(self, mammalName):
    self.mammalName = mammalName
    print(mammalName, 'is a warm-blooded animal.')
 #i wrote this!!! look at me go
  def bark(self):
    print(self.mammalName + " barks")
# child class
class Dog(Mammal):
  def __init__(self):
    print('Dog has four legs.')
    super().__init__('Dog')
    super().bark()
    
d1 = Dog()
