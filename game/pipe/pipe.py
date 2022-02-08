from raylib import *
import random
import pyray

class object:
    
    pipe_x = []
    pipe_y = []
    pipe_color = []
    
    for i in range(0,5):
        new_pipe_x = random.randint(0,200)
        new_pipe_y = random.randint(0,200)
        new_pipe_color = random.randint(0,255), random.randint(0,255), random.randint(0,255) 
        
        pipe_x.append(new_pipe_x)
        
        pipe_y.append(new_pipe_y)
        
        
    def __init__(self, x, y , width, height):
        self.x = x
        self.y = y
        self.width = width
        self.hieght = hieght
        self.color = color

    def pipeloader():
        

        
        for i in range(0,2):
            

            pyray.draw_rectangle(object.pipe_x[i],object.pipe_y[i], 20, 20, WHITE)







