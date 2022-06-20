class GameStats:
    """Track statistics for Alien Invasion."""

    def __init__(self, ai_game):
        self.settings = ai_game.settings
        self.reset_stats()

        self.game_active = False

        # High score should never be reset.
        self.high_score = self.get_high_score()
        self.level = 1

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
    
    def get_high_score(self):
        """Reads saved high score from file and returns it"""
        with open('Python/Alien Invasion/high_score.txt', 'r') as high_score_file:
            high_score = high_score_file.read()
            high_score = high_score.rstrip()
            high_score_file.close()   
        return int(high_score)