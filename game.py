from email.mime import image
import pygame
from gameObject import GameObject
from player import Player
from enemy import Enemy

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
        self.player = Player(375, 700, 50, 50, 'assets/player.png', 5)
        
        # Enemy
        self.enemy = Enemy(50, 600, 50, 50, 'assets/enemy.png', 5)


    def draw_objects(self):
        self.game_window.fill(self.black_color)        
        
        self.game_window.blit(self.background.image, (self.background.x, self.background.y)) # Draw background
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y)) # Draw treasure chest
        self.game_window.blit(self.player.image, (self.player.x, self.player.y)) # Draw player character
        self.game_window.blit(self.enemy.image, (self.enemy.x, self.enemy.y)) # Draw enemy character
        
        
        pygame.display.update()

    def run_game_loop(self):
        
        player_direction = 0
        
        while True:
            # Events Handler
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        player_direction = -1
                    elif event.key == pygame.K_DOWN:
                        player_direction = 1
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                        player_direction = 0
            
            # Execute Logic
            self.player.move(player_direction, self.height)
            self.enemy.move(self.width)
            
            # Update Display
            self.draw_objects()

            self.clock.tick(60)