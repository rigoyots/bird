import raylib 
import random
import pyray


class pipes():
    pipe_x = []
    pipe_y = []
    pipe_color = []
    
    for i in range(0,200):
        new_pipe_x = random.randint(0,800)
        new_pipe_y = random.randint(0,600)
        new_pipe_color = random.randint(0,255), random.randint(0,255), random.randint(0,255) 
        
        pipe_x.append(pipe_x)
        
        pipe_y.append(pipe_y)
        
        
    def __init__(self, x, y , width, height):
        self.x = x
        self.y = y
        self.width = width
        self.hieght = hieght
        self.color = color

    def draw_pipe():
        

        
        for i in range(0,200):
            

            pyray.draw_rectangle(pipes.pipe_x[i],pipes.pipe_y[i], 20, 20, pipes.pipe_color[i])


