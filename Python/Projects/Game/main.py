
import entity as Entity
import combatsystem as CombatSystem


def main():
    
    player = Entity.Player(name="John Gaming",description="The god Player",baseHealth=100,currentHealth=100,baseStrengh=10,baseDexterity=10,isAlive=True)
    monster = Entity.Monster("Monster","A Monster",100,100,10,10,True)

    while monster.currentHealth > 0:
        
        CombatSystem.CombatSystem.combatState(player,monster)
        CombatSystem.CombatSystem.attack(CombatSystem.CombatSystem,player,monster)

main()