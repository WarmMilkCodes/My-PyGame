import pygame

class Game:
    def __init__(self):

        self.width = 800
        self.height = 800
        self.white_color = (255,255,255)

        self.game_window = pygame.display.set_mode((self.width, self.height))

        # Background
        self.background_image = pygame.image.load('assets/background.png')
        self.background_image_scaled = pygame.transform.scale(self.background_image, (self.width, self.height))


        # Treasure
        self.treasure_image = pygame.image.load('assets/treasure.png')
        self.treasure_image_scaled = pygame.transform.scale(self.treasure_image, (50, 50))

        self.clock = pygame.time.Clock()
    

    def draw_objects(self):
        self.game_window.fill(self.white_color)        
        self.game_window.blit(self.background_image_scaled, (0,0))
        self.game_window.blit(self.treasure_image_scaled, (375,50))
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