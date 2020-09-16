class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self,screen,ship,bullet,alien):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 15
        self.bullet_height = 15
        self.bullet_color = (130,160,60)
        self.bullets_allowed = 10

        # Alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 50
        # fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
