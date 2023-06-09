import pygame

class Ship:
    # class to manage the ship

    def __init__(self, ai_game):
        # initalize ship and set its starting position

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # load ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # start each new ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom


        # store a decimal value for the ships horizontal position
        self.x = float(self.rect.x)

        # movement flag
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False

    
    def update(self):
        # update ships position based on movement flag
        # update ships x value, not rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x

    
    def blitme(self):
        # draw ship at its current location
        self.screen.blit(self.image, self.rect)


    def center_ship(self):
        """ center the ship at the bottom of the screen """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)