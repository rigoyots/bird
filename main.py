from raylib import *
from game.pipe.pipe import *
from game.bird.bird import *
import pyray









def main():
   
    
   

    
    
    
   
    pyray.init_window(800,600, "spawn")
    SetWindowState(FLAG_VSYNC_HINT)

    while not WindowShouldClose():
        # Bird
        Bird.draw_bird()
        Bird.move_bird()
        Bird.bird_out_of_bounds()
    
       
       # Pipe
        object_pipe_1.pipeloader()
        object_pipe_2.pipeloader()
        object_pipe_3.pipeloader()
        objects.move_pipes_X()
        objects.move_pipes_up_down()
        objects.bounds()


        pyray.clear_background(BLACK)
        pyray.end_drawing()

    pyray.close_window()

if __name__ == "__main__":
    main()
