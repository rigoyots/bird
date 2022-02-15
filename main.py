from raylib import *
from game.pipe.pipe import *
from game.Bird.bird import *
from game.audio.audio import *
from game.picture.pictures import *
from game.score.score import display_score
from game.color.color import *
import constants
import pyray
import time 

def check_collide():   
    """
    Checks for collisions.
    """    
    game_over = False
    for i in range(1, Obstacle.n_pipes):
        if pyray.check_collision_circle_rec([int(bird.x), int(bird.y)], bird.r,[Bottom.x[i],Bottom.y[i], Bottom.width[i], Bottom.height[i]] ):
           bird.y = Obstacle.y[i]
           bird.x = Obstacle.x[i]
           
           game_over = True   

        if pyray.check_collision_circle_rec([int(bird.x), int(bird.y)], bird.r,[Obstacle.x[i],Obstacle.y[i], Obstacle.width[i], Obstacle.height[i]] ):
           bird.y = Obstacle.y[i]
           bird.x = Obstacle.x[i]
          
           game_over = True

    return game_over

def main():
    """
    Runs the game.
    """
    pyray.init_window(800,600, "Flappy Penguin")
    SetWindowState(FLAG_VSYNC_HINT)
    keep_score = 0

    #Bird picture 
    p = Pictures.bird_pic()

    #Bottom pipe picture
    p_p = Pictures.pipe_2()

    #top pipe picture
    p_d_p = Pictures.pipe_1()

    #auidio
    flap = Audio.audio()
    gameover = Audio.audio_1()
   
    while not WindowShouldClose():
        #checking if game is over 
        check_collide()
        game_over = check_collide()
        
        #audio
        if IsKeyPressed(KEY_SPACE):
            if not game_over:
                pyray.play_sound(flap)
        if not game_over:
            pyray.play_sound(gameover)
        
        #score vaules
        keep_score += bird.y / 100000
        if keep_score >= 20:
            keep_score += .01
        score = str(int(keep_score))

        # Bird
        Bird.draw_bird()
        pyray.draw_texture(p, int(bird.x -10) , int(bird.y -10 ) , WHITE)
        Bird.move_bird()
        Bird.bird_out_of_bounds()

        # Pipe top
        Obstacle.bounds(game_over)
        Obstacle.make_pipe()
        Obstacle.animate(p_d_p)
        Obstacle.move_pipes_X(game_over, keep_score)

        #Bottom pipe
        Bottom.bounds(game_over)
        Bottom.make_pipe()
        Bottom.animate(p_p)
        Bottom.move_pipes_X(game_over, keep_score)

        #background
        pyray.clear_background(RAYWHITE)
        pyray.end_drawing()

        #SOCRE AND CHECK POINTS
        check_collide()
        display_score(game_over, score)

    #unload all data 
    pyray.unload_sound(gameover)        
    pyray.unload_sound(flap)
    pyray.close_audio_device()
    pyray.close_window()

if __name__ == "__main__":
    main()