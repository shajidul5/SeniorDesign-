#!/usr/bin/pyton3
import pygame as sc
from gui.maze import Maze
con=.2 #complexity
dens=.2 #density
maze=Maze(50,30,con,dens) #initiate object
print(maze)
sc.init() 
screen=sc.display.set_mode((750,525))
quit=False
font=sc.font.SysFont(None ,24 )
text=font.render("Right key:changes maze",True,(0,128,0))
text1=font.render("Down Key: Increases Density",True,(0,128,0))
text2=font.render("Up Key:Increases complexity",True,(0,128,0))

Cw=15 #cell width
while not quit:
    #events
    for event in sc.event.get():
        if event.type==sc.QUIT:
            quit=True
    pressed=sc.key.get_pressed()
    if pressed[sc.K_RIGHT]:
        maze=Maze(50,30,con,dens)
    elif pressed[sc.K_UP]:
        con=con+.02
        maze=Maze(50,30,con,dens)
    elif pressed[sc.K_DOWN]:
        dens=dens+.02
        maze=Maze(50,30,con,dens)
  
    #logic and render 
    screen.fill((255,255,255))
    screen.blit(text,(0,455))
    screen.blit(text1,(0,505))
    screen.blit(text2,(0,480))
    screen.blit(font.render(( str(round(con,2))),True,(0,128,0)),(250,480))
    screen.blit(font.render((str(round(dens,2))),True,(0,128,0)),(250,505))
    
    x1=0
    y1=0
    for a in range(0,maze.get_W()):
        for b in range(0,maze.get_H()):
            if maze.get_Value(b,a)==0: #road
                #print(x1,y1) 
                sc.draw.rect(screen,(128,128,128),sc.Rect(y1,x1,Cw,Cw))
                sc.draw.rect(screen,(128,128,128),sc.Rect(y1,x1,Cw,Cw))
            else: #walls
                sc.draw.rect(screen,(130,82,1),sc.Rect(y1,x1,Cw,Cw))
            x1=x1+Cw
        y1=y1+Cw
        x1=0 
   
    sc.display.flip() 
    
