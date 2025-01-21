Tic-Tac-Toe Game
This project is a terminal-based Tic-Tac-Toe (X and O) game. It allows two players to play the game, and the goal is to form three consecutive marks (either X or O) in a row, column, or diagonal.

Description
In this game, two players take turns to place their marks ("X" and "O") on a 3x3 game board. The game ends when one player wins by forming a line of three consecutive marks, or the game ends in a draw.

Requirements
This project is built using Python 3.x. The following software is required to run the game:

Python 3.x (https://www.python.org/downloads/)
Installation
To set up the project on your local machine, follow these steps:

Clone the repository:
'''git clone https://github.com/your-username/tictactoe.git'''
Navigate to the project directory:
'''cd tictactoe'''
Usage
To start the game:
python main.py
Once the game starts, players will take turns choosing a position from 1 to 9 to place their mark on the game board.

The game will end when there is a winner or the game ends in a draw.

Functions
main(): Controls the main game loop, handles user input, and checks the game status.
check_winner(board): Checks if there is a winner on the game board and returns the winner.
display(board): Displays the current state of the game board.
Example of the Game
mathematica
     |     |     
  X  |  O  |  X  
-----+-----+-----
     |     |     
  O  |  X  |  O  
-----+-----+-----
     |     |     
  X  |  O  |  X  
     |     |     

Winner X
Features
Simple and intuitive interface: The game runs in the terminal, making it easy to play and understand.
Winner detection: The game detects and announces the winner or if the game ends in a draw.
Input validation: The program ensures that the user enters valid positions (1-9) and handles invalid inputs accordingly.

