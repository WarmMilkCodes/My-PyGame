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
        
        
        # Enemies
        self.enemies = [
            Enemy(0, 600, 50, 50, 'assets/enemy.png', 5),
            Enemy(750, 400, 50, 50, 'assets/enemy.png', 5),
            Enemy(0, 200, 50, 50, 'assets/enemy.png', 5),
        ]
        
        
   
        
    def draw_objects(self):
        self.game_window.fill(self.black_color)        
        
        self.game_window.blit(self.background.image, (self.background.x, self.background.y)) # Draw background
        self.game_window.blit(self.treasure.image, (self.treasure.x, self.treasure.y)) # Draw treasure chest
        self.game_window.blit(self.player.image, (self.player.x, self.player.y)) # Draw player character
        #self.game_window.blit(self.enemy.image, (self.enemy.x, self.enemy.y)) # Draw one enemy character
        
        for enemy in self.enemies:
            self.game_window.blit(enemy.image, (enemy.x, enemy.y)) # Draw each enemy from enemies list line 31
        
        
        pygame.display.update()
        
        
        
    def move_objects(self, player_direction):
            self.player.move(player_direction, self.height)
            for enemy in self.enemies:
                enemy.move(self.width)
        
        
        
    def detect_collision(self, object_1, object_2):
       ''' if object_1.y > (object_2.y + object_2.height):
            return False
        elif (object_1.y + object_1.height) < object_2.y:
            return False
        
        if object_1.x > (object_2.x + object_2.width):
            return False
        elif (object_1.x + object_1.width) < object_2.x:
            return False
        
        return True
    
        if object_1.y < (object_2.y + object_2.height) and (object_1.y + object_1.height) > object_2.y and object_1.x < (object_2.x + object_2.width) and (object_1.x + object_1.width) > object_2.x:
            return True
        else:
            return False'''
        
    

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
            self.move_objects(player_direction)
            
            # Update Display
            self.draw_objects()
            
            # Detect Collisions
            if self.detect_collision(self.player, self.enemies):
                return
            elif self.detect_collision(self.player, self.treasure):
                return

            self.clock.tick(60)