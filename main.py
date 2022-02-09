from raylib import *
from game.pipe.pipe import *
from game.bird.bird import *
import pyray









def main():
   
    
   
  
    
    
    
   
    pyray.init_window(800,600, "spawn")
    SetWindowState(FLAG_VSYNC_HINT)

    while not WindowShouldClose():
<<<<<<< HEAD
        
        
        obstacle.make_pipe()
        obstacle.move_pipes_X()
        obstacle.bounds()
        bottom.make_pipe()
        bottom.move_pipes_X()
        bottom.bounds()
      
=======
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
>>>>>>> 539b110aafd1531544d8a77723fec1dc396e473e


        pyray.clear_background(BLACK)
        pyray.end_drawing()

    pyray.close_window()

if __name__ == "__main__":
    main()
