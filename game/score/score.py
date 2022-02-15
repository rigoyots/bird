from raylib import *
import pyray
import time 
from bird.constants import *

def display_score(game_over, score): 
    """
    Displays score and says game over when the game ends.
    """  
    if not game_over:
        DrawText(bytes("score: ", encoding='utf8'), 10, 250, int(60), GREEN)
        DrawText(bytes(score, encoding='utf8'), 250, 250, int(60), GREEN)
    
    if game_over:
        DrawText(bytes("game over", encoding='utf8'), 50, 250, int(120), RED)
        end = time.time()