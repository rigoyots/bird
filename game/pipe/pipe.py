from raylib import *
import random
import pyray




class obstacle:
    
    """ 
    List of vairbles for obstacle class
    """
    speed_of_pipe = 300
    n_pipes = 7
    bounds_left = -100
    bounds_right = 900

    x = [0]
    y = []
    width = []
    height = [150]

    for i in range(0,n_pipes):
        """
        makes new pipes 
        """
        new_x = x[i] + 200
        new_y = int(0) 
        new_width = int(50)
        new_height = 250 

        x.append(int(new_x))
        y.append(int(new_y))
        width.append(int(new_width))
        height.append(int(new_height))

       


    def __init__(self, color):
        self.color = color 



    def make_pipe():
      
        for i in range(2,obstacle.n_pipes):
            """
            DRAWS out all the pipes on the screen
            """
            pyray.draw_rectangle(obstacle.x[i], obstacle.y[i], obstacle.width[i], obstacle.height[i], WHITE)

       


    def move_pipes_X(game_over, score):
      
          if not game_over:
            for i in range(1,obstacle.n_pipes):
                if score <= 10:
                     obstacle.x[i] -= int((obstacle.speed_of_pipe - 50)  * GetFrameTime())
                if score >= 10 :
                    obstacle.x[i] -= int((obstacle.speed_of_pipe + 0)  * GetFrameTime())
                if score >= 15:
                     obstacle.x[i] -= int((obstacle.speed_of_pipe + 100)  * GetFrameTime())
                if score >= 20 :
                    obstacle.x[i] -= int((obstacle.speed_of_pipe + 200)  * GetFrameTime())

       


            
     
    def bounds(game_over):
        if not game_over:
            for i in range(2,obstacle.n_pipes):
                if obstacle.x[i] <= obstacle.bounds_left:
                    obstacle.x[i] = int(obstacle.bounds_right)
                    obstacle.y[i] = int(random.randint(-100, 50))
    
    def animate(p_p):
       
        """
       puts the image on top of the pipe
        """
        for i in range(2,7):
        
       

            pyray.draw_texture(p_p, int(obstacle.x[i]) , int(obstacle.y[i] - 30 ) , WHITE)

       
             
             


       
            
class bottom():
    
    
    """ 
    List of vairbles for obstacle class
    """
    
    n_pipes = obstacle.n_pipes 
    bounds_left = -100
    bounds_right = 900
    x = [0]
    y = []
    width = []
    height = [150]


   

    for i in range(0,n_pipes):
        
        new_x = x[i] + 200
        new_y = int(500) 
        new_width = int(50)
        new_height = 250

        x.append(int(new_x))
        y.append(int(new_y))
        width.append(int(new_width))
        height.append(int(new_height))

       


    def __init__(self, color):
        self.color = color 



    def make_pipe():
      
        for i in range(2,obstacle.n_pipes):
            """
            DRAWS out all the pipes on the screen
            """
            pyray.draw_rectangle(bottom.x[i], bottom.y[i], bottom.width[i], bottom.height[i], GREEN)

       


    def move_pipes_X(game_over, score):
        """
        MOVES all the pipes along the x axis
        """
        if not game_over:
            for i in range(1,obstacle.n_pipes):
                if score <= 10:
                     bottom.x[i] -= int((obstacle.speed_of_pipe - 50)  * GetFrameTime())
                if score >= 10 :
                    bottom.x[i] -= int((obstacle.speed_of_pipe + 0)  * GetFrameTime())
                if score >= 15:
                     bottom.x[i] -= int((obstacle.speed_of_pipe + 100)  * GetFrameTime())
                if score >= 20 :
                    bottom.x[i] -= int((obstacle.speed_of_pipe + 200)  * GetFrameTime())

       


            
     
    def bounds(game_over):
        
        """
        gives a limit to x axis for the pipes
        """
        if not game_over:
            for i in range(2,obstacle.n_pipes):
                if bottom.x[i] <= obstacle.bounds_left:
                    bottom.x[i] = int(obstacle.bounds_right)
                    bottom.y[i] = int(random.randint(400, 550))


    def animate(p_p):
        """
       puts the image on top of the pipe
        """
        
        for i in range(2,7):
        
       

            pyray.draw_texture(p_p, int(bottom.x[i] ) , int(bottom.y[i]  ) , WHITE)

       
             





