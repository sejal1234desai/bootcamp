# 09_game_state_persistence.py

import pickle

class Game:
    def __init__(self, level, score, player_name):
        self.level = level
        self.score = score
        self.player_name = player_name

    def __str__(self):
        return f"Player: {self.player_name}, Level: {self.level}, Score: {self.score}"

    def save_state(self, filename):
        # Serialize the game state to a file
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
        print("Game state saved successfully.")

    @classmethod
    def load_state(cls, filename):
        # Deserialize the game state from a file
        with open(filename, 'rb') as f:
            game_state = pickle.load(f)
        return game_state

# Create a Game instance
game = Game(level=5, score=3000, player_name="Sejal Desai")

# Save the game state to a file
game.save_state("game_state.pkl")

# Simulate a new session (reset game state)
new_game = Game(level=1, score=0, player_name="Sejal Desai")

print("\nNew game state:")
print(new_game)

# Load the previously saved game state
restored_game = Game.load_state("game_state.pkl")

print("\nRestored game state:")
print(restored_game)
