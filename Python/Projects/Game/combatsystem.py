import entity

class CombatSystem():

    def __init__(self):
        pass

    def combatState(attacker: entity, defender : entity):
        print(defender.name)
        print(defender.currentHealth)

    def applyDamage(attacker:entity,defender:entity, damage : int):

        defender.currentHealth -= damage

        if defender.currentHealth <= 0:
            defender.isAlive = False
        
        if not defender.isAlive:
            print("enemy resisted")

    def attack(self, attacker: entity, target : entity):
        damageDealt = attacker.baseStrenght + 10 #magic number for now
        
        self.applyDamage(attacker,target,damageDealt)