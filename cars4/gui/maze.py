#!/usr/bin/python3
import numpy
import pygame as sc
sc.init()
from numpy.random import random_integers as rand
from gui.states import States
from gui.car import Car
class Maze: 
    def __init__(self,w=20,h=20,complexity=.75,density=.75):
        self.font=sc.font.SysFont(None ,24 )
        self.text=self.font.render("Right key:changes maze",True,(0,128,0))
        self.text1=self.font.render("Down Key: Increases Density",True,(0,128,0))
        self.text2=self.font.render("Up Key:Increases complexity",True,(0,128,0))
        self.car=Car(10,10,1,1) #ill make it more OOP later
        States.__init__(self)
        self.w=w
        self.h=h
        self.maze=self.build_Maze(self.w,self.h,complexity,density)  
       #doubling road
       # temp1=[]
       # maxCount=0
       # count=2
       # sw=[]
       # for a in range(0,h):
       #     sw.append(1)           
       # temp1.append(sw) 

       # for z in range(1,h-1):
         #   subtemp=[]
         #   subtemp.append(1)
         #   for x in range(1,w-1):
         #       if self.maze[z][x-1]==1 and self.maze[z][x+1]==1 and self.maze[z][x]==1:
         #           subtemp.append(1) 
         #           count=count+1   
         #       if self.maze[z][x-1]==1 and self.maze[z][x+1]==1 and self.maze[z][x]==0:
         #           subtemp.append(0) 
         #           subtemp.append(0) 
         #           count=count+2
         #   subtemp.append(1)
         #   temp1.append(subtemp)
         #   if (maxCount<count):
         #       maxCount=count
         #       count=2
         #   count=2
        
        #for a1 in temp1:
        #    if len(a1)<maxCount:
        #        tempnum=len(a1)
        #        while tempnum<maxCount:
        #            tempnum=tempnum+1
        #            a1.append(1)
        #rq=[]
        #for sq in range(0,maxCount):
        #    rq.append(1)
        #temp1.append(rq)       
        #self.maze=temp1
        #print("pass all")        
    def build_Maze(self,w=50,h=30,complexity=.75,density=.75):
        self.complexity=complexity
        complexity=int(complexity*(5*(w+h)))
        self.density=density
        density=int(density*((w//2)*(h//2)))
        maze=[] 
        for a in range(0,h):
            temp=[]
            for b in range(0,w):
                temp.append(0)
            maze.append(temp)

        for i in range(0,w):
            for j in range(0,h):
                if(i==0 or i==(w-1)): 
                    maze[j][i]=1
                if(j==0 or j==(h-1) ):
                    maze[j][i]=1
               # print(self.maze[j][i],end=" ")
           # print('\n')

        for i in range(0,density):
            x,y=rand(0,(w-1)//2)*2,rand(0,(h-1)//2)*2
            maze[y][x]=1
            for j in range(complexity):
                next_to=[]
                if x>1:
                    next_to.append((y,x-2))
                if x<20-2:
                    next_to.append((y,x+2))
                if y>1:
                    next_to.append((y-2,x))
                if y<20-2:
                    next_to.append((y+2,x))
                if len(next_to):
                   y1,x1=next_to[rand(0,len(next_to)-1)]
                   if maze[y1][x1]==0:
                        maze[y1][x1]=1
                        maze[y1+(y-y1)//2][x1+(x-x1)//2]=1
                        x,y=x1,y1
        return maze
        
    def get_Maze(self):
        return self.maze
    def __str__(self):
        temp=""
        for b in self.maze:
            temp=temp+((str)(b))+"\n"
        return temp
    def get_W(self):
        return self.w
    def get_H(self):
        return self.h
    def get_Value(self,y,x):
        #height=y x=width
        #print("y=="+((str)(y)),end="")
        #print(" x=="+((str)(x)))
        return self.maze[y][x]
    def get_cons(self):
        return self.complexity
    def get_dens(self):
        return self.density
    def get_event(self,event):
        if event.type == sc.KEYDOWN:
#            print("in maze loop")
            if event.key==sc.K_RIGHT:
                self.car=Car(10,10,1,1)
                self.maze=self.build_Maze(50,30,self.complexity,self.density) #builds new maze
            elif event.key==sc.K_UP:
                self.car=Car(10,10,1,1)
                self.inc_con()
                self.maze=self.build_Maze(50,30,self.complexity,self.density)
            elif event.key==sc.K_DOWN:
                self.inc_dens()
                self.car=Car(10,10,1,1)
                self.maze=self.build_Maze(50,30,self.complexity,self.density)  
           #car ill make it more OOP late
            if event.key==sc.K_a and self.get_Value(int(self.car.get_x()),int(self.car.get_y())-1)==0: #UP
                self.car.m_u()
            if event.key==sc.K_d and self.get_Value(int(self.car.get_x()),int(self.car.get_y())+1)==0: #DOWN
                self.car.m_d()
            if event.key==sc.K_w and self.get_Value(int(self.car.get_x())-1,int(self.car.get_y()))==0: #Left
                self.car.m_l()
            if event.key==sc.K_s and self.get_Value(int(self.car.get_x())+1,int(self.car.get_y()))==0: #right
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
        x1=0
        y1=0
        Cw=15
        for a in range(0,self.get_W()):
            for b in range(0,self.get_H()):
                if self.get_Value(b,a)==0: #road
                    #print(x1,y1) 
                    sc.draw.rect(screen,(128,128,128),sc.Rect(y1,x1,Cw,Cw))
                    sc.draw.rect(screen,(128,128,128),sc.Rect(y1,x1,Cw,Cw))
                else: #walls
                    sc.draw.rect(screen,(130,82,1),sc.Rect(y1,x1,Cw,Cw))
                x1=x1+Cw
            y1=y1+Cw
            x1=0 
        z1=int(self.car.get_x())*15
        z2=int(self.car.get_y())*15
        sc.draw.rect(screen,(0,0,255),sc.Rect(z2,z1,self.car.get_h(),self.car.get_w()))


        screen.blit(self.text,(0,455))
        screen.blit(self.text1,(0,505))
        screen.blit(self.text2,(0,480))
        screen.blit(self.font.render(( str(round(self.complexity,2))),True,(0,128,0)),(250,480))
        screen.blit(self.font.render((str(round(self.density,2))),True,(0,128,0)),(250,505))

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





