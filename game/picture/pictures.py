
from raylib import *
import pyray




def pipe_1():
    pipe_pic = pyray.load_image("downpipe.png")
    pyray.image_resize(pipe_pic, 50, 300)
    p_d_p = pyray.load_texture_from_image(pipe_pic)
    pyray.unload_image(pipe_pic)
    return p_d_p


def pipe_2():
    pipe_pic = pyray.load_image("pipe.png")
    pyray.image_resize(pipe_pic, 50, 300)
    p_p = pyray.load_texture_from_image(pipe_pic)
    pyray.unload_image(pipe_pic)
    return p_p

def bird_pic():
    flappy = pyray.load_image("flappy.png")
    pyray.image_resize(flappy, 40, 40)
    p = pyray.load_texture_from_image(flappy)
   
   
    pyray.unload_image(flappy)
    return p 
   