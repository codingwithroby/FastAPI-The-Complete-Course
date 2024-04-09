from Enemy import *

zombie = Enemy('Zombie', 10, 1)

print(f'{zombie.get_type_of_enemy()} has {zombie.health_points} health points and can do attack of {zombie.attack_damage}')

zombie.talk()
zombie.walk_forward()
zombie.attack()

# ----- Next Step -------

ogre = Enemy('Ogre', 20, 3)
print(f'{ogre.get_type_of_enemy()} has {ogre.health_points} health points and can do attack of {ogre.attack_damage}')

ogre.talk()
ogre.walk_forward()
ogre.attack()

