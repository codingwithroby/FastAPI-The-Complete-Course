from Zombie import *
from Ogre import *

zombie = Zombie(10, 1)

print(f'{zombie.get_type_of_enemy()} has {zombie.health_points} health points and can do attack of {zombie.attack_damage}')

zombie.talk()
zombie.walk_forward()
zombie.attack()
zombie.spread_disease()

ogre = Ogre(20, 3)
print(f'{ogre.get_type_of_enemy()} has {ogre.health_points} health points and can do attack of {ogre.attack_damage}')

ogre.talk()
