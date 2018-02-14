#!/usr/bin/python3
import numpy
from numpy.random import random_integers as rand
class Maze: 
    def __init__(self,w=20,h=20,complexity=.75,density=.75):
        self.maze=[]
        self.w=w
        self.h=h
        self.complexity=int(complexity*(5*(w+h)))
        self.density=int(density*((w//2)*(h//2)))
        for a in range(0,h):
            temp=[]
            for b in range(0,w):
                temp.append(0)
            self.maze.append(temp)

        for i in range(0,w):
            for j in range(0,h):
                if(i==0 or i==(w-1)): 
                    self.maze[j][i]=1
                if(j==0 or j==(h-1) ):
                    self.maze[j][i]=1
               # print(self.maze[j][i],end=" ")
           # print('\n')

        for i in range(0,self.density):
            x,y=rand(0,(w-1)//2)*2,rand(0,(h-1)//2)*2
            self.maze[y][x]=1
            for j in range(self.complexity):
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
                   if self.maze[y1][x1]==0:
                        self.maze[y1][x1]=1
                        self.maze[y1+(y-y1)//2][x1+(x-x1)//2]=1
                        x,y=x1,y1
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
#0=empty space
#1=wall
#a=Maze()
#b=a.get_Maze() 
#for b in a.get_Maze():
 #   print(b)





