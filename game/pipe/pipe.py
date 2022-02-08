from raylib import *
import random
import pyray

class objects:
  
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = WHITE


    def move_pipes_X():

        pipe_1.x -= int(300 *GetFrameTime())
        pipe_2.x -= int(300 *GetFrameTime())
        pipe_3.x -= int(300 *GetFrameTime())

    def move_pipes_up_down():

        if pipe_1.x <= -20:
            
            pipe_1.height = random.randint(50, 100)

        
        if pipe_2.x <= -20:
            
            pipe_2.height = random.randint(50, 150)

        
        if pipe_3.x <= -20:
            
            pipe_3.height = random.randint(50, 200)

    
    def bounds():
        
        if pipe_1.x <= -20:
            pipe_1.x = 900
            
        
        if pipe_2.x <= -20:
            pipe_2.x = 900
           
        
        if pipe_3.x <= -20:
            pipe_3.x = 900
            


  


class object_pipe_1(objects):
   
    def __init__(self,x,y, width, height, color):
        super().__init__(width, height, color)

        self.x = x
        self.y = y
    
    def pipeloader():
        

        
    
            

        pyray.draw_rectangle(pipe_1.x,pipe_1.y, 50, pipe_1.height, WHITE)

pipe_1 = object_pipe_1(200, 0, 200, 50, WHITE)



class object_pipe_2(objects):
  
    def __init__(self,x,y, width, height, color):
        super().__init__(width, height, color)
        self.x = x
        self.y = y


    def pipeloader():
        

        
       
            
        pyray.draw_rectangle(pipe_2.x,pipe_2.y, 50,  pipe_2.height, WHITE)

pipe_2 = object_pipe_1(400, 0, 200, 50, WHITE)

class object_pipe_3(objects):
   
    def __init__(self,x,y,width, height, color):
        super().__init__(width, height, color)
        self.x = x
        self.y = y


    def pipeloader():
        

        
        
            

        pyray.draw_rectangle(pipe_3.x,pipe_2.y, 50,  pipe_3.height, WHITE)

pipe_3 = object_pipe_1(600, 0, 200, 50, WHITE)







