from raylib import *
from game.pipe.pipe import *
from game.Bird.bird import *
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
        obstacle.bounds()
        obstacle.make_pipe()
        obstacle.move_pipes_X()
        bottom.bounds()
        bottom.make_pipe()
        bottom.move_pipes_X()

        pyray.clear_background(BLACK)
        pyray.end_drawing()

    pyray.close_window()

if __name__ == "__main__":
    main()
