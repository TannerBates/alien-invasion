class Settings:
    # a class to store all settings for alien invasion


    def __init__(self):
        # initalize the games settings 
        # screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (260, 260, 260)

        # bullet settings 
        self.bullet_speed = 8.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3


        # ships settings
        self.ship_speed = 4
        self.ship_limit = 3

        # alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 15

        # fleet_direction of 1 represents right; -1 represents left
        self.fleet_direction = 1