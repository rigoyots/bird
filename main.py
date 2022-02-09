from raylib import *
from game.pipe.pipe import *
from game.Bird.bird import *
import pyray




def check_collid():   
    
    game_over = False
    for i in range(1, obstacle.n_pipes):
        if pyray.check_collision_circle_rec([int(bird.x), int(bird.y)], bird.r,[bottom.x[i],bottom.y[i], bottom.width[i], bottom.height[i]] ):
           bird.y = obstacle.y[i]
           bird.x = obstacle.x[i]
           
           game_over = True      
        if pyray.check_collision_circle_rec([int(bird.x), int(bird.y)], bird.r,[obstacle.x[i],obstacle.y[i], obstacle.width[i], obstacle.height[i]] ):
           bird.y = obstacle.y[i]
           bird.x = obstacle.x[i]
          
           game_over = True

    return game_over

def display_score(game_over, score): 
    
    
    
    if not game_over:
        DrawText(bytes("score: ", encoding='utf8'), 10, 250, int(60), YELLOW)
        DrawText(bytes(score, encoding='utf8'), 250, 250, int(60), YELLOW)
    
    if game_over:
        DrawText(bytes("game over", encoding='utf8'), 50, 250, int(120), RED)
        end = time.time()



def main():
   
    
   
  
    
    keep_score = 0
    
   
    pyray.init_window(800,600, "Flappy Ball")
    SetWindowState(FLAG_VSYNC_HINT)

    while not WindowShouldClose():
        
        keep_score += bird.y / 100000
        score = str(int(keep_score))
        
        check_collid()
        game_over = check_collid()
        # Bird
        Bird.draw_bird()
        Bird.move_bird()
        Bird.bird_out_of_bounds()
    
       
       # Pipe
        obstacle.bounds(game_over)
        obstacle.make_pipe()
        obstacle.move_pipes_X(game_over)
        bottom.bounds(game_over)
        bottom.make_pipe()
        bottom.move_pipes_X(game_over)

        pyray.clear_background(BLACK)
        pyray.end_drawing()
        
        
        
      
        
        
        check_collid()
        display_score(game_over, score)

        


    pyray.close_window()

if __name__ == "__main__":
    main()


