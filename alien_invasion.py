import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """class to manage game assets and behaviour."""
    def __init__(self):
        """initialize the game and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.screen=pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        #set bg color
        self.bg_color=(56,4,73)
    
    def run_game(self):
        """start the main loop for the game"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        #Watch for keyboards and mouse events
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    #move the ship to the right
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        #redraw the screen during each pass through loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
         #make the most recently drawn screen visible
        pygame.display.flip()           

if __name__ == '__main__':
    #make a game instance and run the game.
    ai=AlienInvasion()
    ai.run_game()