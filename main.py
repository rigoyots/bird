from raylib import *
from pipe import *
import pyray









def main():
   
    
   

    
    
    
   
    pyray.init_window(800,600, "spawn")
    SetWindowState(FLAG_VSYNC_HINT)

    while not WindowShouldClose():
        

        object.pipeloader()
  
        pyray.clear_background(BLACK)
        pyray.end_drawing()

    pyray.close_window()

if __name__ == "__main__":
    main()
