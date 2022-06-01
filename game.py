from email.mime import image
import pygame
from gameObject import GameObject

class Game:
    def __init__(self):

        self.width = 800
        self.height = 800
        self.white_color = (255,255,255)

        self.game_window = pygame.display.set_mode((self.width, self.height))

        # Background
        self.background = GameObject(0,0, self.width, self.height, 'assets/background.png')

        # Treasure
        self.treasure = GameObject(375,50, 50, 50, 'assets/treasure.png')

        self.clock = pygame.time.Clock()
    

    def draw_objects(self):
        self.game_window.fill(self.white_color)        
        self.game_window.blit(self.background.image, (self.background.x, self.background.y))
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y))
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