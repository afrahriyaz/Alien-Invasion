class Settings:
    """A class to store all settings for alien invasion"""
    def __init__(self):
        """Initialize the game settings"""
        #Screen settings
        self.screen_width=1200
        self.screen_height=800
        self.bg_color=(56,4,73)

        #Ship settings
        self.ship_speed = 2.5

        #bullet settings
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255,255,0)