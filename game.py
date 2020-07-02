import pygame
import blits
import time

pygame.init()  
WS =(1000, 500)
screen = pygame.display.set_mode(WS)
frame_rate =  20
clock = pygame.time.Clock()
pygame.init()
font = pygame.font.SysFont("bitstreamverasans", 30)
def main() :
    global screen
    snakeobj = blits.snake(screen , WS)
    run = True
    while run  :
        run = snakeobj.operate(pygame.event.get())
        clock.tick(frame_rate)
        screen.blit(font.render(str(snakeobj.len - 1), True, (0,0,255)), (0, 0))
        pygame.display.flip()
        screen.fill([0 , 0 ,0])

    game_score = font.render("Score " + str(snakeobj.len - 1) ,  True, (60,130,120))
    while True : 
        for event in pygame.event.get() : 
            if event.type == pygame.QUIT:  
                exit() 
        screen.blit(game_score, (0 , 0 ))
        pygame.display.flip()

if __name__ == "__main__" : 
    main()
