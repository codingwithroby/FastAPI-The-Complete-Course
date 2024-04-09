class Enemy:

    '''
    Goal: Show Encapsulation
    - Display Zombie walking, speaking and attacking.
    - Display Zombie getting their health and attacking
    - Create constructor
    - Encapsulation for getting the type of enemy
    - Create a new Enemy Ogre who needs more attack than the Zombie
    '''

    def __init__(self, type_of_enemy, health_points = 10, attack_damage = 1):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

    def talk(self):
        print(f"I am a {self.__type_of_enemy}. Be prepared to fight!")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} moves closer to you")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage} damage")  

    def get_type_of_enemy(self):
        return self.__type_of_enemy