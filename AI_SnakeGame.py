"""
AI Snake Game - Main Runner File

This script initializes the Snake game with a selected AI solver
and game mode, then starts the game.

Project: AI Snake Game
"""

# Import required classes from the snake package
from snake.game import Game, GameConf, GameMode

# -------------------------------
# Solver Options
# -------------------------------
# You can switch between different AI strategies

GREEDY_SOLVER = "GreedySolver"        # Fast but may fail in complex paths
HAMILTON_SOLVER = "HamiltonSolver"    # Safe but slower (covers full grid)

# -------------------------------
# Game Mode
# -------------------------------
# NORMAL mode = standard snake gameplay

GAME_MODE = GameMode.NORMAL

# -------------------------------
# Game Configuration Setup
# -------------------------------
def configure_game():
    """
    Creates and configures the game settings.
    Returns:
        GameConf object with selected solver and mode
    """
    config = GameConf()

    # Choose solver (change here if needed)
    config.solver_name = GREEDY_SOLVER

    # Set game mode
    config.mode = GAME_MODE

    return config


# -------------------------------
# Main Function
# -------------------------------
def main():
    """
    Entry point of the AI Snake Game
    Initializes configuration and starts the game
    """
    # Get game configuration
    conf = configure_game()

    # Display selected configuration
    print(f"Solver: {conf.solver_name}")
    print(f"Mode: {conf.mode}")

    # Start the game
    Game(conf).run()


# -------------------------------
# Run the Program
# -------------------------------
if __name__ == "__main__":
    main()