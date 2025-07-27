import random

# TITLE
print("Pokemon Battle Game: 3 vs 3") 

# REVIEW: Pokemon List
pokemon_list = ["Pikachu", "Charizard", "Greninja", "Sceptile", "Snorlex", "Gengar", "Alakazam","Onix", "Gyarados", "Dragonite", "Venusaur", "Blastoise", "Meowth", "Blaziken", "Swellow", "Corphish", "Lucario", "Infernape", "Darkrai", "Muk"]

# HEADING: Pokemon Name & Attacks
pokemon_attack = {
    "Pikachu": {"Thunder Bolt": 20,"Iron Tail": 15,"Quick Attack": 15},
    "Charizard": {"Flamethrower": 15,"Dragon Claw": 25,"Ancient Power": 20},
    "Greninja": {"Water Pledge" : 20, "Water Pulse": 15, "Water Shuriken": 25},
    "Sceptile": {"Leaf Blade": 25, "X Scissor": 20, "Bullet Seed": 10},
    "Snorlex": {"Hyper Beam": 25, "Body Slam" : 20, "Ice Punch": 10},
    "Gengar" : {"Shadow Ball": 20, "Night Shade": 15, "Dark Pulse": 10},
    "Alakazam": {"Psychic":25, "Confusing": 20, "Focus Punch":10},
    "Onix": {"Iron Tail":20, "Earthquake":15, "Rock Tomb":10},
    "Gyarados": {"Hyper Beam": 20, "Fire Blast" : 15, "Giga Impact": 10},
    "Dragonite": {"Draco Meteor": 25, "Thunder Bolt": 10, "Dragon Breath": 20},
    "Venusaur": {"Vine Whip": 10, "Solar Beam" : 20, "Giga Impact": 15},
    "Blastoise": {"Hydro Cannan": 25, "Aura Sphere":20, "Water Gun": 10},
    "Meowth": {"Scratch": 15, "Slash": 10, "Duniya Ko Tabahi Se Bachane Ke Liye Sabhi Logo Ko Ek Sath Lane Ke Liye Sabko Batane Ke Liye Ki Hum Kya Kar Sakte Hai Puri Kaynat Ko Apni Muthi Main Kar Sakte Hai Jessie James Team Rocket Humari Lumbi Hai Height Surrender Karo Ya Fir Karo Humse Fight Chode Gey Nahi Day Ho Ya Night": 20},
    "Blaziken": {"Fire Spin": 25, "Double Kick":15, "Aerial Ace":10},
    "Swellow": {"Aerial Ace": 25, "Steal Wing": 15, "Brave Bird": 10},
    "Corphish": {"Metal Claw": 20, "Bubble Beam":15, "Sludge Bomb": 10},
    "Lucario": {"Aura Sphere": 25, "Extreme Speed":15, "Shadow Ball": 10},
    "Infernape": {"Overheat": 25, "Fire Punch": 20, "Flame Wheel":15},
    "Darkrai": {"Confuse Ray": 30, "Night Shade": 25, "Dream Eater":15},
    "Muk": {"Body Slam": 20, "Sludge Bomb": 15, "Gunk Shot": 10}
}

# HEADING : Player 1 Code
while True: 
    player_1 = input(f"\nPlayer Enter Your Name: ").capitalize()
    if player_1 == "":
        print("\nPlease Enter A Valid Name")
    else:
        break

# NOTE: Pokemon Selection Process
i = 0
n = 1
registered_pokemon = []
while i < 3:
    print(f"\nPokemon's available for selection {n}: {sorted(pokemon_list)}")
    sel_pok= input(f"Enter Your Pokemon {n}: ").capitalize()

    if sel_pok in pokemon_list:
        print(f"[{sel_pok}] Registered as pokemon {n}")
        registered_pokemon.append(sel_pok)
        pokemon_list.remove(sel_pok)
        i += 1
        n += 1
    else:
        print("Please Enter Correct Name")

print("\n\n----- Pokemon Registration Completed -----")

print(f"\n\n{player_1}'s Registered Pokemon's are: {registered_pokemon}")

# NOTE: Computer's Choice
random.shuffle(pokemon_list)
computer_choice = random.sample(pokemon_list, 3)
print(f"Computer's Registered Pokemon's are: {computer_choice}")

# TITLE: Game Logic

rounds = 1
results = []

player_wins = 0
computer_wins = 0

while registered_pokemon and computer_choice:
    player_hp = 100
    computer_hp = 100

    while True:
        player1_pokemon_select = input(f"\n\n{player_1} choose your pokemon for round {rounds} between: {registered_pokemon}: ").capitalize()

        if player1_pokemon_select in registered_pokemon:
            print(f"\n\n{player_1} select ['{player1_pokemon_select}'] for round {rounds}")
            computer_pokemon_select = random.choice(computer_choice)
            print(f"Computer select ['{computer_pokemon_select}'] for round {rounds}")
            print(f"\n\n------------ Round {rounds} ------------\nFight Between: [{player1_pokemon_select} vs {computer_pokemon_select}]")
            break
        else:
            print("Enter Valid Pokemon Name")

    while player_hp > 0 and computer_hp > 0:
        while True:
            player1_attack = input(f"\n\nChoose your attack {list(pokemon_attack[player1_pokemon_select].keys())}: ").title()
            if player1_attack in pokemon_attack[player1_pokemon_select]:
                break
            else:
                print(f"Enter valid {player1_pokemon_select}'s attack")
            
        computer_attack = random.choice(list(pokemon_attack[computer_pokemon_select].keys()))

        print(f"\nStatement: {player1_pokemon_select} used {player1_attack} against {computer_pokemon_select}, and {computer_pokemon_select} fought back with {computer_attack}.")           

        player_hp -= pokemon_attack[computer_pokemon_select][computer_attack]
        computer_hp -= pokemon_attack[player1_pokemon_select][player1_attack]

        player_hp = max(player_hp, 0)
        computer_hp = max(computer_hp, 0)

        print(f"\nScore:>                       {player1_pokemon_select} HP-{player_hp} || {computer_pokemon_select} HP-{computer_hp}")

        print("\n----------------------------------------------------------------------------------------------------")

        if player_hp <= 0 and computer_hp <= 0:
            print(f"\nIts a draw! {player1_pokemon_select} and {computer_pokemon_select} Both Pokemon Cant Fight")
            results.append(f"Round {rounds} --> result is draw eliminated pokemon's are: ('{player1_pokemon_select}') and ('{computer_pokemon_select}') - Both Lose")
            break
        elif player_hp <= 0:
            print(f"\n{computer_pokemon_select} wins! {player1_pokemon_select} Lose! ")
            results.append(f"Round {rounds} --> winner ('{computer_pokemon_select}') and Loser ('{player1_pokemon_select}') - Computer Wins")
            computer_wins += 1
            break
        elif computer_hp <= 0:
            print(f"\n{player1_pokemon_select} wins! {computer_pokemon_select} Lose")
            results.append(f"Round {rounds} --> winner ('{player1_pokemon_select}') and Loser ('{computer_pokemon_select}') - {player_1} Wins")
            player_wins += 1
            break
    if player_hp <= 0:
        if player1_pokemon_select in registered_pokemon:
            registered_pokemon.remove(player1_pokemon_select)
    if computer_hp <= 0:
        if computer_pokemon_select in computer_choice:
            computer_choice.remove(computer_pokemon_select)

    rounds += 1 
        
print(f"\n\n------Game Over! Result Are------")
for result in results:
    print(result)

print(f"\n\n-----Final Result-----")
if player_wins > computer_wins:
    print(f"{player_1} wins the match by {player_wins} - {computer_wins}")
    print(f"\n{player_1} has {registered_pokemon} available to fight.")
    print(f"Computer has no Pokemon left to fight.")
elif computer_wins > player_wins:
    print(f"\nComputer wins the match by {computer_wins} - {player_wins}")
    print(f"Computer has {computer_choice} available to fight.")
    print(f"{player_1} has no Pokemon left to fight.")
elif computer_wins == player_wins:
    print(f"Its a draw by {player_wins} - {computer_wins}")
    print(f"\nBoth {player_1} and Computer are out of Pokemon! No one left to fight.")
    
