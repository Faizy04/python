import random
The=['Cat','Tree','Book','Beach','Mountain']
Story=['Runs','Reads','Swims','Climbs','Dances']
Is=['Beautiful','Playful','Tall','Peaceful','Adventurous']
Begins=['Quickly','Quietly','Happily','Carefully','Eagerly']
Here=['Under','On','Near','Between','Above']
Player_health=100
Dragon_health=100
for i in range(20):
    Player=random.randint(5,20)
    dragon=random.randint(5,20)
    print(random.choice(The),random.choice(Story),random.choice(Is),random.choice(Begins),random.choice(Here))
    Player_health=Player_health-Player
    Dragon_health=Dragon_health-dragon

    if Player_health<=0:
        print('Dragon won',)
        print('player health=',Player_health,'\nDragon health=',Dragon_health)
        exit()
    if Dragon_health<=0:
        print('Player health=',Player_health,'\nDragon health=',Dragon_health)
        print('Player won',)
        exit()

    print('player health=',Player_health)
    print('Dragon health=',Dragon_health)