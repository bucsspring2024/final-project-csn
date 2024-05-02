import pygame
import math

class Cloud:
    def __init__ (self, x, y, scale, screen_width):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('assets/Clouds Loop.webp').convert()
        self.width = self.img.get_width()
        self.scroll = 0
        self.tiles = math.ceil(screen_width / self.width) + 1