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

    def draw_bird(self):
        """
        draws the bird
        """
        pyray.draw_circle(int(self.x), int(self.y), self.r, BLACK)

    def move_bird(self):
        """
        moves the bird
        """
        if IsKeyPressed(KEY_SPACE): 
            self.y -= 600 * GetFrameTime()
        elif IsKeyDown(KEY_SPACE):
            self.y -= 600 * GetFrameTime()
        else: #IsKeyUp(KEY_SPACE)
            self.y += 250 * GetFrameTime()


    def bird_out_of_bounds(self):
        """
        checks if the bird is out of bounds
        """
        if self.y <= 0:
            self.y = 2
        elif self.y >= 600:
            self.y = 599

bird = Bird(200, 300, 5)