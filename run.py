from os import system
from state import game_state
from welcome import welcome

# Run welcome function to introduce the game.
#welcome()

# After final turn, assign final game state.
final_state = game_state()

# Announce game over and print final game state.
welcome()
print('\nGAME OVER!\n')
#welcome()
print(final_state)

# Write final game state to JSON file, and open this file.
with open('final_state.json', 'w') as f:
    f.write(final_state)
system('open final_state.json')
