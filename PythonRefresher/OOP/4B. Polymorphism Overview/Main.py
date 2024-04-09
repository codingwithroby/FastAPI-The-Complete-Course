from Animal import *
from Bird import *
from Dog import *


zoo: Animal = []

dog = Animal()
dog2 = Dog()

bird = Bird()

zoo.append(dog)
zoo.append(dog2)
zoo.append(bird)

for animal in zoo:
    animal.talk()

