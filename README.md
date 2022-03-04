# Battle_knight
# Usage
To run the app:

python run.py
Moves are read in from 'moves.txt'.

The output is written to 'final_state.json'.

* moves.txt which uses the input file that indicates the movement of the knight

* startup.py: This file defines the knights and items classes, and the instances of the respective classes. for easy reference it is stored in the object.

* state.py: it consist of the game state, it also create a string in the JSON compatible format, and showing the state of each knight and item.

* move_details.py: Here is where the result of the knight movement and direction is described. it also describe what happens when the knight move to a new position on the borad, or off the board, or if item are picked or dropped and also shows the result if the knight is attacking and if the knight wins or is defeated.

* welcome.py: it creates board state, which appears as an 8x8 board in the command line, with text symbols which indicate the positions of any living knights and also print out the welcome and the board.
