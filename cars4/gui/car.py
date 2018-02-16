#!/usr/bin/python

class Car:
    def __init__(self, w=5,h=5,x=0,y=0):
        self.w=w
        self.h=h
        self.x=x
        self.y=y
    
    def __str__(self):
        temp="x=="+self.x+" y=="+self.y
        return temp
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def m_r(self):
        self.x+=1
        return
    
    def m_l(self):
        self.x-=1
        return 

    def m_u(self):
        self.y-=1
        return
    
    def m_d(self):
        self.y+=1
        return

    def get_w(self):
        return self.w

    def get_h(self):
        return self.h 
