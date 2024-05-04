import pygame
from src import Cloud
from src import Book
from src import Library
from src import Button
from src import Bookshelf
from src import API
from src import FrontDesk
from src import BookSave
from src import Heart
from src import Reset

class Controller :
  
  def __init__(self):
    self.screen_width = 1000
    self.screen_height = 562
    
    self.clock = pygame.time.Clock()
    self.FPS = 60

    self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
    pygame.display.set_caption("Mia's Library")
    self.mainloop()

    
  def mainloop(self):
    pygame.display.init()
    welcome = pygame.image.load('assets/Welcome.png').convert_alpha()
    yes = pygame.image.load('assets/Yes.png').convert_alpha()
    error = pygame.image.load('assets/Error_msg.png').convert_alpha()
    ok = pygame.image.load('assets/Ok.png').convert_alpha()
    
    book = Book.Book(500,250,2.5)
    book2 = BookSave.Book2(200, 200, 5)
    cloud = Cloud.Cloud(500, 400, .5, self.screen_width)
    library = Library.Library(540,350, 1.4)
    welcome_button = Button.Button(500, 282, welcome, 0.25)
    yes_button = Button.Button(500, 370, yes, 0.15)
    bookshelf = Bookshelf.Bookshelf (780, 278, 1.4)
    frontdesk = FrontDesk.FrontDesk (160,429, 1.4)
    heart = Heart.Heart(780,80, 10)
    reset = Reset.Reset(350, 280, 21)
    ok_button = Button.Button (500, 370, ok, 0.15)
    book_tup = API.get_book()

    saved_spells = []
    
    run = True
    while run:
        self.clock.tick(self.FPS)
        
        for i in range(0, cloud.tiles):
            self.screen.blit(cloud.img, (i* cloud.width + cloud.scroll ,0))
        cloud.scroll -= 0.5
        if abs(cloud.scroll) > cloud.width:
            cloud.scroll = 0 
        
        self.screen.blit(library.img, library.rect)
        self.screen.blit (bookshelf.img, bookshelf.rect)
        self.screen.blit(frontdesk.img, frontdesk.rect)
        
        if(yes_button.clicked == False) : 
            self.screen.blit(welcome_button.image, welcome_button.rect)
            self.screen.blit(yes_button.image, yes_button.rect)
            
        
        if book.render == True: 
          book2.render = False
          self.screen.blit(book.img, book.rect)
          self.screen.blit(heart.img, heart.rect)
      
          font = pygame.font.SysFont(None, 35)
          input_rect = pygame.Rect(180, 75, 200, 32)
          color = pygame.Color('white')
          
          text = font.render(book_tup[0], True, (0,0,0))
          input_rect.w = max(100, text.get_width()+10)
          pygame.draw.rect(self.screen, color, input_rect)
          self.screen.blit(text, (input_rect.x+5, input_rect.y+5))
          
          font2 = pygame.font.SysFont(None,28)
          input_rect2 = pygame.Rect(180, 180, 400, 30)
          
          text = font2.render(book_tup[1], True, (0,0,0))
          input_rect2.w = max(100, text.get_width()+10)
          pygame.draw.rect(self.screen, color, input_rect2)
          self.screen.blit(text, (input_rect2.x+5, input_rect2.y+5))

          
          
          
        if book2.render == True : 
            book.render = False
            self.screen.blit(book2.img, book2.rect)
            self.screen.blit(reset.img, reset.rect)
            
            font3 = pygame.font.SysFont(None, 26)
            color = pygame.Color('white')
            start =100
            for x in saved_spells:
                input_rect3 = pygame.Rect(150, start, 400, 32)
                text = font3.render(x, True, (0,0,0))
                input_rect3.w = max(100, text.get_width()+10)
                pygame.draw.rect(self.screen, color, input_rect3)
                start = start + 40
                self.screen.blit(text, (input_rect3.x+5, input_rect3.y+5))
                
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if yes_button.clicked == False and yes_button.rect.collidepoint(pos) == True:
                    yes_button.clicked = True
                    
                if ok_button.clicked == False and ok_button.rect.collidepoint(pos) == True:
                    ok_button.clicked = True
                    
                if bookshelf.rect.collidepoint(pos) == True:
                    if heart.rect.collidepoint(pos) == True:
                        saved_spells.append(str(book_tup[0]))
                        book_tup = API.get_book()
                        
    
                    else:
                        book.render = not book.render
                        book_tup = API.get_book()
                        
                        
                if frontdesk.rect.collidepoint(pos) == True:
                    book2.render = not book2.render
                    
                
                if reset.rect.collidepoint(pos) == True:
                        saved_spells = []
                    
        pygame.display.update()
    pygame.quit()
