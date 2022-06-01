from telnetlib import GA
import pygame
from game import Game

pygame.init()

game = Game()
game.run_game_loop()

pygame.quit()
quit()