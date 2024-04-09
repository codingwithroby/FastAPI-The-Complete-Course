from Enemy import *

class Ogre(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy="Ogre", health_points=health_points, attack_damage=attack_damage)

    def talk(self):
        print("Ogre is slamming hands all around!")
    