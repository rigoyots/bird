
from raylib import *
import pyray


def audio():
    
    """
    loads the sound for the flapping 
    """
    pyray.init_audio_device()
    
    flap = pyray.load_sound("flap.wav")
    
   
    
    pyray.set_sound_volume(flap, 0.5)
    return flap 
    
  


def audio_1():
    """
    Loads sound for game over
    """
    gameover = pyray.load_sound("over.wav")
   

    return gameover