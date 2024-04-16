import pygame
#import your controller

def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()
    
class Book:
    def __init__(self, x, y, img_file):
        self.x = x
        self.y = y
        self.img_file = img_file
        
    def stack_right(self):
        self.x += 100
        
    def stack_left(self):
        self.x += 100
        
class Window:
    def __init__(self, x, y, clouds, screen_length):
        self.x = screen_length
        self.y = screen_length
        self.clouds = clouds
        
    def move_right(self):
        while True:
            self.clouds +=200
        
        
        
        
    
    
