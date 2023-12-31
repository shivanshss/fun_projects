### Setup and Initialization:
        Initialize Pygame.
        Create the game window.
        Load necessary assets (images, sounds, etc.).

### Player Control:
        Handle player input (keyboard and potentially gamepad).
        Move the player character.
        Implement jumping and sprinting mechanics.

### Torch Control:
        Toggle the torch on and off based on player input.

### Maze Generation:
        Implement maze generation logic. You might use libraries like random to create randomized mazes.

### Monster AI:
        Create a monster that follows the player based on their noise level.
        Implement movement and behavior for the monster.

### UI:
        Create UI elements to display callout options and handle input.
        Design and implement the main menu UI.
        
        
## TerrOut Horror Game

Welcome to the TerrOut Horror Game, a thrilling adventure that will test your courage and agility as you navigate through a mysterious maze while avoiding a terrifying monster. Use your skills to outsmart the creature and reach the exit, but be cautious - one wrong move could lead to a gruesome encounter.
## Getting Started

To play the game, you'll need to have Python and the Pygame library installed on your computer. Follow these steps to set up the game:

    Install Python: If you don't have Python installed, download and install it from the official Python website.

    Install Pygame: Open a terminal/command prompt and enter the following command to install Pygame:

    pip install pygame

    Download Game Assets: Download the game assets (player.png and monster.jpeg) and save them in the same directory as the game script.

## How to Play

Run the game script by executing it with Python:

python your_game_script.py

Here's how to play the game:

    Use the W, A, S, D keys to move the player character.
    Press Spacebar to make the player jump.
    Hold down the Left Shift key to activate sprint mode for faster movement.
    Your goal is to navigate through the maze, avoiding walls and obstacles, and reach the exit.
    Beware of the monster! It will chase you, so be quick and strategic to avoid getting caught.
    If the monster catches you, it's game over. Feel free to restart and try again.

## Game Mechanics

    The player's movement speed can be adjusted with the player_speed constant.
    Jumping is controlled by the Spacebar. Adjust the player_jump_power and player_gravity constants to change jump behavior.
    Sprinting is activated by holding down the Left Shift key. Modify the sprint_multiplier constant to change sprint speed.
    The maze is randomly generated using the generate_maze function. Adjust MAZE_WIDTH and MAZE_HEIGHT constants to change maze size.
    The monster's behavior is controlled by the move_monster function. It will chase the player based on their position.

Note: This game is a basic implementation and does not include features like win conditions, complex AI, or advanced gameplay elements. It serves as a starting point for building upon and expanding the game.


## Recursive Backtracking Maze Generator

The Recursive Backtracking Maze Generator is a Python script that creates random maze structures using the recursive backtracking algorithm. This algorithm creates intricate and winding mazes that can be used in games, puzzles, and other applications. The generated mazes are represented using a grid of cells, where walls are denoted by #, paths by empty spaces, entrance by D, and exit by T.
How to Generate Mazes

Follow these steps to use the Recursive Backtracking Maze Generator:

    Run the Script: Open a terminal or command prompt and navigate to the directory where you saved the script. Run the script using the following command:

    python your_script_name.py

    Adjust Maze Dimensions: Inside the script, you can adjust the width and height parameters passed to the generate_maze function. These parameters determine the dimensions of the generated maze.

    View the Generated Maze: The script will display the generated maze in the console. Walls are represented by #, paths by empty spaces, entrance by D, and exit by T.

## Maze Generation Algorithm

The script uses the Recursive Backtracking algorithm to generate mazes. Here's how the algorithm works:

    Initialize a grid of cells, where walls are represented by 1 and paths by 0.
    Start at a random cell and carve a path to neighboring unvisited cells.
    Choose a random unvisited neighboring cell and move to it, carving a path along the way.
    Repeat step 3 until there are no more unvisited neighboring cells.
    Backtrack to the previous cell and repeat step 3 for that cell.
    Continue this process until the entire maze is generated.
