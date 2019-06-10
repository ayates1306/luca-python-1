import random
print("-------------------------TWINS BATTLE SIMULATOR!!!!!-------------------------")
print("")
print("Instructions:")
print("Your options are 'Attack' or 'Heal'. Type these in respectively to make your    move.")
print("To start off, the Twins have 500 health, you have 300 health, and 5 healing     potions which heal 100 health each. Your attack does 50 damage, unless you")
print("land a critical hit, or if you miss (random). Type 'E','N','H' to select Easy,  Normal or Hard and summon the Twins and begin.")
Start = input()
Difficulty = ["E","N","H"]
while Start not in Difficulty:
    print("Type the respective letters (in capitals!) to select difficulty and begin.")
    Start = input()
if Start == "E":
    TwinsHealth = 450
    MaxP_Health = 400
    PlayerHealth = 400
    HealingPotions = 7
    Random_number1 = 6
    Random_number2 = 3
elif Start == "N":
    TwinsHealth = 500
    MaxP_Health = 300
    PlayerHealth = 300
    HealingPotions = 5
    Random_number1 = 5
    Random_number2 = 4
elif Start == "H":
    TwinsHealth = 600
    MaxP_Health = 250
    PlayerHealth = 250
    HealingPotions = 3
    Random_number1 = 4
    Random_number2 = 5
print ("The Twins have awoken!")
while TwinsHealth > 1:
    command = input("What is your move?")
    if command == "Attack":
        if Start == "E":
            Attack = 60
            if Random_number1 == random.randint(1,3):
                Attack = Attack + random.randint(10,30)
                TwinsHealth = TwinsHealth - Attack
                print("You attacked! Critical hit! Dealt" ,Attack, "damage!")
            elif (Random_number2 == random.randint(1,6)):
                    print("Miss!")
            else:
                TwinsHealth = TwinsHealth - Attack
                print("You attacked! Dealt" ,Attack, "damage!")
        elif Start == "N":
            Attack = 50
            if Random_number1 == random.randint(1,4):
                Attack = Attack + random.randint(5,20)
                TwinsHealth = TwinsHealth - Attack
                print("You attacked! Critical hit! Dealt" ,Attack, "damage!")
            elif (Random_number2 == random.randint(1,5)):
                print("Miss!")
            else:
                TwinsHealth = TwinsHealth - Attack
                print("You attacked! Dealt" ,Attack, "damage!")
        elif Start == "H":
            Attack = 40
            if Random_number1 == random.randint(1,5):
                Attack = Attack + random.randint(3,10)
                TwinsHealth = TwinsHealth - Attack
                print("You attacked! Critical hit! Dealt" ,Attack, "damage!")
            elif (Random_number2 == random.randint(1,4)):
                print("Miss!")
            else:
                TwinsHealth = TwinsHealth - Attack
                print("You attacked! Dealt" ,Attack, "damage!")
    elif command == "Heal":
         if HealingPotions > 0:
             PlayerHealth = PlayerHealth + 100
             print("You drank a healing potion! Gained 100 health.")
             HealingPotions = HealingPotions - 1
         elif PlayerHealth > MaxP_Health:
             PlayerHealth = MaxP_Health
             print("Your health is maxed out!")
             HealingPotions = HealingPotions - 1
         else:
            print("You're out of healing potions!")
    print("Twins health is" ,TwinsHealth, "!")
    print("You have" ,HealingPotions, "healing potions left!")
    if TwinsHealth < 1:
        print("The Twins have been defeated!")
        break
    else:
        if Random_number2 == random.randint(1,5):
            print("You dodged the Twins' attack!")
        else:
            TwinsDamage = random.randint(20, 50)
            print ("Twins attacked! Lost" ,TwinsDamage, "health!")
            PlayerHealth = PlayerHealth - TwinsDamage
            print("You have" ,PlayerHealth, "health!")
    if PlayerHealth < 1:
            print("You were slain...")
            break



