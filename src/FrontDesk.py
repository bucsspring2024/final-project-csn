import pygame

class FrontDesk:
       def __init__ (self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('assets/FrontDesk.png')
        self.img = pygame.transform.scale(img, (img.get_width()*scale, img.get_height()*scale))
        self.width = img.get_width()
        self.height = img.get_height()
        self.rect = self.img.get_rect()
        self.rect.center = (x, y)
        self.clicked = False