#!/usr/bin/python3
import numpy
import pygame as sc
from numpy.random import random_integers as rand
from gui.states import States
from gui.car import Car
from gui.BaseMaze import BaseMaze
class Maze: 
    def __init__(self,w=20,h=20,complexity=.75,density=.75):
        sc.init()
        self.font=sc.font.SysFont(None ,24 )
        self.text=self.font.render("Right key:changes maze",True,(0,128,0))
        self.text1=self.font.render("Down Key: Increases Density",True,(0,128,0))
        self.text2=self.font.render("Up Key:Increases complexity",True,(0,128,0))
        self.car=Car(10,10,1,1) 
        States.__init__(self)
        self.w=w
        self.h=h
        self.maze=BaseMaze(self.w,self.h,complexity,density)
        
    def get_Maze(self):
        return self.maze
    def get_W(self):
        return self.w
    def get_H(self):
        return self.h
   # def get_Value(self,y,x):
        #height=y x=width
        #print("y=="+((str)(y)),end="")
        #print(" x=="+((str)(x)))
    #    return self.maze.get[y][x]
    def get_cons(self):
        return self.complexity
    def get_dens(self):
        return self.density
    def get_event(self,event):
        if event.type == sc.KEYDOWN:
            if event.key==sc.K_RIGHT: #re-builds maze
                self.car=Car(10,10,1,1)
                self.maze.re_Construct()                 
            elif event.key==sc.K_UP: #increases complexity
                self.car=Car(10,10,1,1)
                self.maze.inc_com() 
            elif event.key==sc.K_DOWN: #increases density
                self.car=Car(10,10,1,1)
                self.maze.inc_den()   
           #car ill make it more OOP late
            if event.key==sc.K_a and self.maze.get_Value(int(self.car.get_x()),int(self.car.get_y())-1)==0: #UP
                self.car.m_u()
            if event.key==sc.K_d and self.maze.get_Value(int(self.car.get_x()),int(self.car.get_y())+1)==0: #DOWN
                self.car.m_d()
            if event.key==sc.K_w and self.maze.get_Value(int(self.car.get_x())-1,int(self.car.get_y()))==0: #Left
                self.car.m_l()
            if event.key==sc.K_s and self.maze.get_Value(int(self.car.get_x())+1,int(self.car.get_y()))==0: #right
                self.car.m_r()

    def inc_con(self):
        if self.complexity<=1:
            self.complexity+=.02
    def inc_dens(self):
        if self.density<=1:
            self.density+=.02
    def update(self,screen,dt): 
        self.draw(screen)
    def draw(self,screen): #actual drawing goes here
        screen.fill((255,255,255)) 
        sc.draw.rect(screen,(130,82,1),sc.Rect(0,0,750,455))
        x1=0
        y1=0
        Cw=30 #cell width
        for a in range(0,self.get_W()):
            for b in range(0,self.get_H()):
                if self.maze.get_Value(b,a)==0: #road
                    sc.draw.rect(screen,(128,128,128),sc.Rect(y1,x1,Cw,Cw))
                    sc.draw.rect(screen,(128,128,128),sc.Rect(y1,x1,Cw,Cw))
                x1=x1+Cw
            y1=y1+30
            x1=0
             
        z1=int(self.car.get_x())*30
        z2=int(self.car.get_y())*30
        sc.draw.rect(screen,(0,0,255),sc.Rect(z2,z1,self.car.get_h(),self.car.get_w()))


        screen.blit(self.text,(0,455))
        screen.blit(self.text1,(0,505))
        screen.blit(self.text2,(0,480))
        screen.blit(self.font.render(( str(round(self.maze.g_com(),2))),True,(0,128,0)),(250,480))
        screen.blit(self.font.render((str(round(self.maze.g_den(),2))),True,(0,128,0)),(250,505))

        return 
    def cleanup(self):
        #createclean up
        pass
  #    def
#0=empty space
#1=wall
#a=Maze()
#b=a.get_Maze() 
#for b in a.get_Maze():
 #   print(b)





