import gym
from gym.spaces import Discrete
import numpy as np

class MyGameEnv(gym.Env):
    def __init__(self):
        # Define action space (0-9 for D suggestions)
        self.action_space = Discrete(10)

        # Define observation space (history of past 5 X and D pairs)
        self.observation_space = Discrete(100000)  # Adjust representation if needed

        # Initialize game state variables
        self.reset()
    
    def get_state(self):
        # Return the current state (history of past 5 moves as a single integer)
        return sum([10**i * move for i, move in enumerate(self.history[-5:])])

    def reset(self, x_symbols=None):
        # Reset state variables
        self.x_symbol = None
        self.d_suggestion = None
        self.history = []
        self.finished = False

        # If provided pre-fetched X symbols, iterate through them
        if x_symbols is not None:
            self.x_symbol = x_symbols[0]
            self.x_symbols = x_symbols[1:]  # Store remaining symbols for next steps
        else:
            self.x_symbol = np.random.randint(0, 9)  # Fallback to random generation

        self.history.append(self.x_symbol)

        return self.get_state()
    
    def _check_win(self):
        # Check if the D suggestion wins against the current X symbol
        return self.d_suggestion in self._winning_combinations[self.x_symbol]

    def _check_finished(self):
        # Replace with your logic for determining when the game ends
        return len(self.history) >= 10  # Example: game ends after 10 moves

    
    def step(self, action):
        # Validate action (D suggestion)
        if not 0 <= action <= 9:
            raise ValueError("Invalid action taken: {}. Action space is 0-9.".format(action))

        # Update D suggestion and history
        self.d_suggestion = action
        self.history.append(action)

        # Calculate reward based on win/loss
        reward = 0.09 if self._check_win() else -1

        # Check if game is finished (based on your criteria, e.g., length of history)
        self.finished = self._check_finished()

        return self.get_state(), reward, self.finished, {}

    

    
    # Pre-defined winning combinations (as a dictionary)
    _winning_combinations = {
        0: [1, 2, 3, 4, 5, 6, 7, 8, 9],
        1: [0, 2, 3, 4, 5, 6, 7, 8, 9],
        2: [0, 1, 3, 4, 5, 6, 7, 8, 9],
        3: [0, 1, 2, 4, 5, 6, 7, 8, 9],
        4: [0, 1, 2, 3, 5, 6, 7, 8, 9],
        5: [0, 1, 2, 3, 4, 6, 7, 8, 9],
        6: [0, 1, 2, 3, 4, 5, 7, 8, 9],
        7: [0, 1, 2, 3, 4, 5, 6, 8, 9],
        8: [0, 1, 2, 3, 4, 5, 6, 7, 9],
        9: [0, 1, 2, 3, 4, 5, 6, 7, 8]
            
    }