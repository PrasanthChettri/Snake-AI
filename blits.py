import pygame
from random import randint 



class snake() : 
    def __init__(self , screen , WS) : 
        self.WS = WS
        self.screen = screen
        self.dim = 20
        self.len = 1
        self.xc = self.dim  
        self.yc = 0
        self.blocks = [[0 , 0]]
        self.food = [randint(self.dim , WS[0])//self.dim * self.dim ,
                            randint(self.dim , WS[1])//self.dim * self.dim]

    def operate(self,  events) : 
        for event in events : 
            if event.type == pygame.QUIT:  
                return False 
            if event.type == pygame.KEYDOWN : 
                if event.key == pygame.K_LEFT and self.xc != self.dim: 
                    self.xc = -self.dim
                    self.yc = 0
                elif event.key == pygame.K_RIGHT and self.xc != - self.dim:
                    self.xc = self.dim
                    self.yc = 0
                elif event.key == pygame.K_UP and self.yc != self.dim:
                    self.yc = -self.dim 
                    self.xc = 0
                elif event.key == pygame.K_DOWN and self.yc != -self.dim:
                    self.yc = self.dim
                    self.xc = 0

        x = self.blocks[0][0] + self.xc 
        y = self.blocks[0][1] + self.yc
        self.blocks.insert(0 , [x ,y])
        for block in self.blocks[1:] : 
            if block[0] == self.blocks[0][0] and block[1] == self.blocks[0][1] : 
                return False
        if x < 0 or x > self.WS[0] - self.dim or y < 0 or y > self.WS[1] - self.dim : 
            return False 
        if x == self.food[0] and y == self.food[1] : 
            self.food = [randint(self.dim , self.WS[0])//self.dim * self.dim ,
                                randint(self.dim , self.WS[1])//self.dim * self.dim]
            self.len += 1 
        else : 
            self.blocks.pop() 

        self.show()
        return True

    def show(self) : 
        for (x , y)  in self.blocks : 
            pygame.draw.rect(self.screen , [255 , 255 , 255] , [x ,
                                y , self.dim , self.dim])
        pygame.draw.rect(self.screen , [69 , 69 , 69] , [self.food[0] , self.food[1] , 
                            self.dim , self.dim])

