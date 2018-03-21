from numpy.random import random_integers as rand


class BaseMaze:
    def __init__(self,w=30,h=50,com=.75,den=.75):
        self.w=w
        self.h=h
        self.com=com
        self.den=den
        self.ConstructMaze()
        print(self)
        
        
    def ConstructMaze(self):
        shape = ((self.h// 2) * 2 + 1, (self.w// 2) * 2 + 1)
        
        complexity=int(self.g_com()*(5*(shape[0] + shape[1])))
        density=int(self.g_den()*((shape[0] // 2) * (shape[1] // 2)))
        
        self.maze=[] 
        for a in range(0,self.h):
            temp=[]
            for b in range(0,self.w):
                temp.append(0)
            self.maze.append(temp)

        for i in range(0,self.w):
            for j in range(0,self.h):
                if(i==0 or i==(self.w-1)): 
                    self.maze[j][i]=1
                if(j==0 or j==(self.h-1) ):
                    self.maze[j][i]=1
               # print(self.maze[j][i],end=" ")
           # print('\n')

        for i in range(density):
            x,y=rand(0, shape[1] // 2) * 2, rand(0, shape[0] // 2) * 2
            self.maze[y][x]=1
            for j in range(complexity):
                next_to=[]
                if x>1:
                    next_to.append((y,x-2))
                if x<shape[1]-2:
                    next_to.append((y,x+2))
                if y>1:
                    next_to.append((y-2,x))
                if y<shape[0]-2:
                    next_to.append((y+2,x))
                if len(next_to):
                   y1,x1=next_to[rand(0,len(next_to)-1)]
                   print("y== "+(str)(y1)+" x=="+(str)(x1))
                   if self.maze[y1][x1]==0:
                        self.maze[y1][x1]=1
                        self.maze[y1+(y-y1)//2][x1+(x-x1)//2]=1
                        x,y=x1,y1

    def re_Construct(self):
        self.ConstructMaze()
    def inc_com(self):
        if (self.com<.98):
            self.com+=.02
            self.ConstructMaze()    
    def inc_den(self):
        if (self.den<.98):
            self.den+=.02
            self.ConstructMaze()
    def __str__(self): #for debugging
        temp=""
        for b in self.maze:
            temp=temp+((str)(b))+"\n"
        return temp        
    
    def g_h(self): #get h
        return (int)(self.h)
    
    def g_w(self): #get w
        return (int)(self.w)
    
    def g_den(self):#get density
        return self.den
    
    def g_com(self):#get complexity
        return self.com
    def get_Maze(self):
        return self.maze
    def get_Value(self,y,x):
        return self.maze[y][x]

