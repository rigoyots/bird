from raylib import *
import pyray 
from color.color import *
from bird.constants import *


class Bird():
    """
    The Bird class is the character that the user will play. 

    Responsibilites:
        Draws the bird.
        Moves the bird.
        Checks if the bird is out of bounds.

    Attributes:
        self.x = x
        self.y = y
        self.r = r
    """

    def __init__(self, x, y, r):
        """
        Initializes the Bird class.
        """
        self.x = x
        self.y = y
        self.r = r

    def draw_bird():
        """
        Draws the bird.
        """
        pyray.draw_circle(int(bird.x), int(bird.y), bird.r, BLACK)

    def move_bird():
        """
        Moves the bird.
        """
        if IsKeyPressed(KEY_SPACE): 
            bird.y -= 600 * GetFrameTime()
        elif IsKeyDown(KEY_SPACE):
            bird.y -= 600 * GetFrameTime()
        else: #IsKeyUp(KEY_SPACE)
            bird.y += 250 * GetFrameTime()


    def bird_out_of_bounds():
        """
        Checks if the bird is out of bounds.
        """
        if bird.y <= 0:
            bird.y = 2
        elif bird.y >= 600:
            bird.y = 599

bird = Bird(200, 300, 5)