from raylib import *
import random
import pyray

class Obstacle():
    """ 
    List of vairbles for the Obstacle class.

    Responsibilites:
        makes the pipe
        moves the pipe
        checks the bounds
        animates the pipes

    Attributes:
        self.color = color
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
        Makes new pipes.
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
        """
        Initializes the Pipe class.
        """
        self.color = color 

    def make_pipe():
        """
        Makes a new pipe.
        """
        for i in range(2,Obstacle.n_pipes):
            # DRAWS out all the pipes on the screen
            pyray.draw_rectangle(Obstacle.x[i], Obstacle.y[i], Obstacle.width[i], Obstacle.height[i], WHITE)

    def move_pipes_X(game_over, score):
        """
        Moves the pipes.
        """
        if not game_over:
            for i in range(1,Obstacle.n_pipes):
                if score <= 10:
                     Obstacle.x[i] -= int((Obstacle.speed_of_pipe - 50)  * GetFrameTime())
                if score >= 10 :
                    Obstacle.x[i] -= int((Obstacle.speed_of_pipe + 0)  * GetFrameTime())
                if score >= 15:
                     Obstacle.x[i] -= int((Obstacle.speed_of_pipe + 100)  * GetFrameTime())
                if score >= 20 :
                    Obstacle.x[i] -= int((Obstacle.speed_of_pipe + 200)  * GetFrameTime())      
     
    def bounds(game_over):
        """
        Sets the bounds of the game.
        """
        if not game_over:
            for i in range(2,Obstacle.n_pipes):
                if Obstacle.x[i] <= Obstacle.bounds_left:
                    Obstacle.x[i] = int(Obstacle.bounds_right)
                    Obstacle.y[i] = int(random.randint(-100, 50))
    
    def animate(p_p):
        """
        Puts the image on top of the pipe.
        """
        for i in range(2,7):
            pyray.draw_texture(p_p, int(Obstacle.x[i]) , int(Obstacle.y[i] - 30 ) , WHITE)       
                         
class Bottom():
    """ 
    List of vairbles for Bottom class.

    Responsibilites:
        makes the pipe
        moves the pipe
        checks the bounds
        animates the pipes

    Attributes:
        self.color = color
    """
    n_pipes = Obstacle.n_pipes 
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
        """
        Initializes the Bottom class.
        """
        self.color = color 

    def make_pipe():
        """
        Makes a pipe.
        """
        for i in range(2,Obstacle.n_pipes):
            # DRAWS out all the pipes on the screen
            pyray.draw_rectangle(Bottom.x[i], Bottom.y[i], Bottom.width[i], Bottom.height[i], GREEN)

    def move_pipes_X(game_over, score):
        """
        Moves all the pipes along the x axis.
        """
        if not game_over:
            for i in range(1,Obstacle.n_pipes):
                if score <= 10:
                     Bottom.x[i] -= int((Obstacle.speed_of_pipe - 50)  * GetFrameTime())
                if score >= 10 :
                    Bottom.x[i] -= int((Obstacle.speed_of_pipe + 0)  * GetFrameTime())
                if score >= 15:
                     Bottom.x[i] -= int((Obstacle.speed_of_pipe + 100)  * GetFrameTime())
                if score >= 20 :
                    Bottom.x[i] -= int((Obstacle.speed_of_pipe + 200)  * GetFrameTime())

    def bounds(game_over):        
        """
        Gives a limit to x axis for the pipes.
        """
        if not game_over:
            for i in range(2,Obstacle.n_pipes):
                if Bottom.x[i] <= Obstacle.bounds_left:
                    Bottom.x[i] = int(Obstacle.bounds_right)
                    Bottom.y[i] = int(random.randint(400, 550))

    def animate(p_p):
        """
        Puts the image on top of the pipe.
        """
        for i in range(2,7):
            pyray.draw_texture(p_p, int(Bottom.x[i] ) , int(Bottom.y[i]  ) , WHITE)