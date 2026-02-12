class Entity:

    def __init__(self,name,description,baseHealth=100,currentHealth=100,baseStrengh=10,baseDexterity=10,isAlive = True):
        self.name = name
        self.description = description
        self.baseHealth = baseHealth
        self.currentHealth = currentHealth
        self.baseStrenght = baseStrengh
        self.baseDexterity = baseDexterity
        self.isAlive = isAlive

class Player(Entity):
    def __init__(self, name, description, baseHealth, currentHealth, baseStrengh, baseDexterity,isAlive):
        super().__init__(name, description, baseHealth, currentHealth, baseStrengh, baseDexterity,isAlive)
    
class Monster(Entity):
    def __init__(self, name, description, baseHealth, currentHealth, baseStrengh, baseDexterity,isAlive):
        super().__init__(name, description, baseHealth, currentHealth, baseStrengh, baseDexterity,isAlive)