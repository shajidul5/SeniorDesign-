import pygame

pygame.init()
screen = pygame.display.set_mode((400,300))
done=False
x=30
y=30

while not done:
        #events
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done=True                
        temp=2
        pressed=pygame.key.get_pressed()
        #loop compute changes in the game world
        if pressed[pygame.K_UP]: y-=3
        if pressed[pygame.K_DOWN]: y+=3
        if pressed[pygame.K_LEFT]: x-=3
        if pressed[pygame.K_RIGHT]: x+=3
        if pressed[pygame.K_SPACE]: done=True
        #render, print out into the world
        screen.fill((0,0,0))
        pygame.draw.rect(screen,(0,128,255),pygame.Rect(x,y,60,60))
	#first argument is the surface instance, second argumet is color in RGB, what to draw and the coordiantes 
        pygame.display.flip()
