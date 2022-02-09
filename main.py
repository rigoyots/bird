from raylib import *
from game.pipe.pipe import *
import pyray









def main():
   
    
   
  
    
    
    
   
    pyray.init_window(800,600, "spawn")
    SetWindowState(FLAG_VSYNC_HINT)

    while not WindowShouldClose():
        
        
        obstacle.make_pipe()
        obstacle.move_pipes_X()
        obstacle.bounds()
        bottom.make_pipe()
        bottom.move_pipes_X()
        bottom.bounds()
      


        pyray.clear_background(BLACK)
        pyray.end_drawing()

    pyray.close_window()

if __name__ == "__main__":
    main()
