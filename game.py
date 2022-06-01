from email.mime import image
import pygame
from gameObject import GameObject
from player import Player

class Game:
    def __init__(self):

        self.width = 800
        self.height = 800
        self.white_color = (255,255,255)
        self.black_color = (0,0,0)

        self.game_window = pygame.display.set_mode((self.width, self.height))

        # Background
        self.background = GameObject(0, 0, self.width, self.height, 'assets/background.png')

        # Treasure
        self.treasure = GameObject(375, 50, 50, 50, 'assets/treasure.png')

        # Clock
        self.clock = pygame.time.Clock()
    
        # Player
        self.player = Player(375, 700, 50, 50, 'assets/player.png', 10)


    def draw_objects(self):
        self.game_window.fill(self.black_color)        
        
        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
        self.game_window.blit(self.player.image, (self.player.x, self.player.y))
        
        
        pygame.display.update()

    def run_game_loop(self):
        while True:
            # Handle Events
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
            # Execute Logic
            # Update Display
            self.draw_objects()

            self.clock.tick(60)