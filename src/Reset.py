import pygame

class Reset:
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('assets/Reset.jpg')
        self.img = pygame.transform.scale(img, (img.get_width()/scale, img.get_height()/scale))
        self.rect = self.img.get_rect()
        self.rect.center = (x, y)
        self.render = False