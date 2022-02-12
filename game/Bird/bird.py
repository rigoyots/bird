from raylib import *
import pyray 

class Bird:
    """
    The bird class is the character that the user will play. 

    Responsibilites:
        draws the bird
        moves the bird
        checks if the bird is out of bounds

    Attributes:
        self.x = x
        self.y = y
        self.r = r
    """

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def draw_bird():
        """
        draws the bird
        """
        pyray.draw_circle(int(bird.x), int(bird.y), bird.r, BLACK)

    def move_bird():
        """
        moves the bird
        """
        if IsKeyPressed(KEY_SPACE): 
            bird.y -= 600 * GetFrameTime()
        elif IsKeyDown(KEY_SPACE):
            bird.y -= 600 * GetFrameTime()
        else: #IsKeyUp(KEY_SPACE)
            bird.y += 250 * GetFrameTime()


    def bird_out_of_bounds():
        """
        checks if the bird is out of bounds
        """
        if bird.y <= 0:
            bird.y = 2
        elif bird.y >= 600:
            bird.y = 599

bird = Bird(200, 300, 5)