
from raylib import *
import pyray


def audio():
    pyray.init_audio_device()
    
    flap = pyray.load_sound("flap.wav")
    
   
    
    pyray.set_sound_volume(flap, 0.5)
    return flap 
    
  


def audio_1():
 
    gameover = pyray.load_sound("over.wav")
   

    return gameover