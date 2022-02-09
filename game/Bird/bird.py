from raylib import *
import pyray 

class Bird:
    """
    Bird
    """

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def draw_bird():
        """
        draws the bird
        """
        pyray.draw_circle(int(bird.x), int(bird.y), bird.r, WHITE)

    def move_bird():
        """
        moves the bird
        """
        if IsKeyPressed(KEY_SPACE): 
            bird.y -= 400 * GetFrameTime()
        elif IsKeyDown(KEY_SPACE):
            bird.y -= 400 * GetFrameTime()
        elif IsKeyUp(KEY_SPACE):
            bird.y += 100 * GetFrameTime()


    def bird_out_of_bounds():
        """
        checks if the bird is out of bounds
        """
        if bird.x <= 0:
            bird.x = 2
        elif bird.x >= 800:
            bird.x = 599

bird = Bird(400, 550, 5)