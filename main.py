import pygame
import math
#import your controller

def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
  
screen_width = 1000
screen_height = 562

clock = pygame.time.Clock()
FPS = 1

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mia's Library")

welcome = pygame.image.load('assets/Welcome.png').convert_alpha()
yes = pygame.image.load('assets/Yes.png').convert_alpha()

class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.clicked = False
    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

class Cloud:
    def __init__ (self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load('assets/Clouds Loop.webp').convert()
        self.width = self.img.get_width()
        self.scroll = 0
        self.tiles = math.ceil(screen_width / self.width) + 1

class Library:
       def __init__ (self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load('assets/Library.png')
        self.img = pygame.transform.scale(img, (img.get_width()*scale, img.get_height()*scale))
        self.width = img.get_width()
        self.height = img.get_height()
        self.rect = self.img.get_rect()
        self.rect.center = (x, y)
        
        
        
#class Book:
    #def __init__(self, x, y, scale):
        #pygame.sprite.Sprite.__init__(self)
        #img = pygame.image.load('assets/Open_Book.jpg')
        #self.img = pygame.transform.scale(img, (img.get_width()/scale, img.get_height()/scale))
        #self.rect = self.img.get_rect()
        #self.rect.center = (x, y)
        
#book = Book(500,400,4)
cloud = Cloud(500, 400, .5)
library = Library(540,350, 1.4)
welcome_button = Button(500, 282, welcome, 0.25)
yes_button = Button(500, 370, yes, 0.15)

run = True
while run:
    
    clock.tick(FPS)
    for i in range(0,cloud.tiles):
        screen.blit(cloud.img, (i* cloud.width + cloud.scroll ,0))
    cloud.scroll -= 5
    if abs(cloud.scroll) > cloud.width:
        cloud.scroll = 0
    
    screen.blit(library.img, library.rect)
    screen.blit(welcome_button.image, welcome_button.rect)
    screen.blit(yes_button.image, yes_button.rect)
    
    #screen.blit(book.img, book.rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
pygame.quit()