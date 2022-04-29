# World Module
# CSRMUTT Self-Driving Car Framework
# Version 1.1
# Author : Songphon Klabwong(songphon@rmutt.ac.th)

from framework import *
import random

class World():
    def __init__(self, width,height):
        '''initialize world with random value'''
        self.size = (width,height)
        self.data = []
        self.landmarks = []
        self.__build_random_world(width,height)

        self.print_world()

    def __build_random_world(self,w,h):
        for i in range(h):#loop through height
            l = [0] * w
            for j in range(w):#loop through width
                v = random.randint(1,10)
                if  v <= 2 : l[j] = v*20
            self.data.append(l)

    def set_obstacle_at(self,(x,y)):
        if x <0 or x > self.size[0] or y < 0 or y > self.size[1]:
            raise ValueError("Invalid position.")

    def set_landmark(self, landmarks):
        self.landmarks = landmarks

    def get_view(self,(x,y),vis=2):
        '''get the view of world by position and visibility'''
        view = []
        sight = vis*2+1
        for j in range(sight):
            row = [0]*sight
            for i in range(sight):
                u = (x+i-vis)%self.size[1]
                v = (y+j-vis)%self.size[0]
                row[i] = self.data[v][u]
            view.append(row)
                
        return view

    def get_value_at(self,(x,y)):
        if x <0 or x > self.size[0] or y < 0 or y > self.size[1]:
            raise ValueError("Invalid position.")
        return self.data[y][x]

    def set_world(self, world):
        self.data = world
        self.size = (len(world[0]),len(world))

    def print_view(self,(x,y),vis=2):
        view = self.get_view((x,y),vis)
        for r in view:
            print(r)

    def print_world(self):
        for row in self.data:
            print(row)

    def draw(self, canvas):
        '''draw world to the canvas'''
        sw = canvas.get_width()/self.size[0]
        sh = canvas.get_height()/self.size[1]
        for j in range(self.size[1]): #loop through lines
            for i in range(self.size[0]): #loop through each line
                if self.data[j][i] > 0:
                    #draw color block
                    c = max(0,255-self.data[j][i]*16)
                    color = (c,c,c)
                    pygame.draw.rect(canvas, color,(i*sw, j*sh,sw, sh))

                #draw landmarks
                for m in self.landmarks:
                    pygame.draw.rect(canvas, (255,0,0), (m[0]*sw, m[1]*sh,sw, sh))

                #draw hollow cell with border
                pygame.draw.rect(canvas, (0,0,0),(i*sw, j*sh,sw, sh),1)

        return canvas
