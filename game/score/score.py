
from raylib import *
import pyray
import time 



def display_score(game_over, score): 
    
    
    
    if not game_over:
        DrawText(bytes("score: ", encoding='utf8'), 10, 250, int(60), YELLOW)
        DrawText(bytes(score, encoding='utf8'), 250, 250, int(60), YELLOW)
    
    if game_over:
        DrawText(bytes("game over", encoding='utf8'), 50, 250, int(120), RED)
        end = time.time()
