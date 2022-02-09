from raylib import *
from game.pipe.pipe import *
from game.Bird.bird import *
import pyray
import time 



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
    
    
   
 
    
    pyray.init_window(800,600, "Flappy Ball")
    SetWindowState(FLAG_VSYNC_HINT)
    
    #Bird picture 
    flappy = pyray.load_image("flappy.png")
    pyray.image_resize(flappy, 20, 20)
    p = pyray.load_texture_from_image(flappy)
   
    pyray.unload_image(flappy)
    #bottom pipe 
    pipe_pic = pyray.load_image("pipe.png")
    pyray.image_resize(pipe_pic, 50, 300)
    p_p = pyray.load_texture_from_image(pipe_pic)
   
    pyray.unload_image(pipe_pic)
   #top pip
    pipe_pic = pyray.load_image("downpipe.png")
    pyray.image_resize(pipe_pic, 50, 300)
    p_d_p = pyray.load_texture_from_image(pipe_pic)
   
    pyray.unload_image(pipe_pic)
    
    keep_score = 0

    while not WindowShouldClose():
        
        
        
        keep_score += bird.y / 100000
        score = str(int(keep_score))
        
        check_collid()
        game_over = check_collid()
        # Bird
        Bird.draw_bird()
        pyray.draw_texture(p, int(bird.x -10) , int(bird.y -10 ) , WHITE)
        Bird.move_bird()
        Bird.bird_out_of_bounds()
    
       
       # Pipe
        obstacle.bounds(game_over)
        
        
        
        obstacle.make_pipe()
        obstacle.animate(p_d_p)
        obstacle.move_pipes_X(game_over)
        bottom.bounds(game_over)
        
        bottom.make_pipe()
        bottom.animate(p_p)
        
       

        bottom.move_pipes_X(game_over)
        

        pyray.clear_background(RAYWHITE)
        pyray.end_drawing()
        
        
        
      
        
        
        check_collid()
        display_score(game_over, score)

        


    pyray.close_window()

if __name__ == "__main__":
    main()


