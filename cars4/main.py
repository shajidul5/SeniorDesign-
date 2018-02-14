#!/usr/bin/pyton3
import pygame as sc
from gui.maze import Maze

maze=Maze(35,30,.8,.8) #initiate object
print(maze)
sc.init() 
screen=sc.display.set_mode((750,500))
quit=False
font=sc.font.SysFont(None ,24 )
text=font.render("Pressed right key to change maze",True,(0,128,0))
Cw=10 #cell width
while not quit:
    #events
    for event in sc.event.get():
        if event.type==sc.QUIT:
            quit=True
    pressed=sc.key.get_pressed()
    if pressed[sc.K_RIGHT]:
        maze=Maze(35,30,.8,.8)
  
    #logic and render
    
    screen.fill((0,0,0))
    screen.blit(text,(150,400))
    x1=Cw
    y1=Cw
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
        x1=Cw 
   
    sc.display.flip() 
    
