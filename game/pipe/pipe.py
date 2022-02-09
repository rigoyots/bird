from raylib import *
import random
import pyray




class obstacle:
    speed_of_pipe = 300
    n_pipes = 7
    bounds_left = -100
    bounds_right = 900

    x = [0]
    y = []
    width = []
    height = [110]

    for i in range(0,n_pipes):
        
        new_x = x[i] + 200
        new_y = int(0) 
        new_width = int(50)
        new_height = height[i]  

        x.append(int(new_x))
        y.append(int(new_y))
        width.append(int(new_width))
        height.append(int(new_height))

       


    def __init__(self, color):
        self.color = color 



    def make_pipe():
      
        for i in range(2,obstacle.n_pipes):
            
            pyray.draw_rectangle(obstacle.x[i], obstacle.y[i], obstacle.width[i], obstacle.height[i], WHITE)

       


    def move_pipes_X():
      
        
        for i in range(1,obstacle.n_pipes):
            obstacle.x[i] -= int(obstacle.speed_of_pipe * GetFrameTime())

       


            
     
    def bounds():
        
        for i in range(2,obstacle.n_pipes):
            if obstacle.x[i] <= obstacle.bounds_left:
                obstacle.x[i] = int(obstacle.bounds_right)
                obstacle.height[i] = int(random.randint(150, 350))
             


       
            
class bottom():
    n_pipes = obstacle.n_pipes 
    bounds_left = -100
    bounds_right = 900
    x = [0]
    y = []
    width = []
    height = [110]

    for i in range(0,n_pipes):
        
        new_x = x[i] + 200
        new_y = int(500) 
        new_width = int(50)
        new_height = 600

        x.append(int(new_x))
        y.append(int(new_y))
        width.append(int(new_width))
        height.append(int(new_height))

       


    def __init__(self, color):
        self.color = color 



    def make_pipe():
      
        for i in range(2,obstacle.n_pipes):
            
            pyray.draw_rectangle(bottom.x[i], bottom.y[i], bottom.width[i], bottom.height[i], RED)

       


    def move_pipes_X():
      
        
        for i in range(1,obstacle.n_pipes):
            bottom.x[i] -= int(obstacle.speed_of_pipe * GetFrameTime())

       


            
     
    def bounds():
        
        for i in range(2,obstacle.n_pipes):
            if bottom.x[i] <= obstacle.bounds_left:
                bottom.x[i] = int(obstacle.bounds_right)
                bottom.y[i] = int(obstacle.height[i] * 1.6) 
             






