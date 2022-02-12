
from raylib import *
import pyray

class audio:
    """
    The Audio class contains the code to produce the game's sounds.
    """
    def audio():
        """
        Loads the sound for the flapping.
        """
        pyray.init_audio_device()
        flap = pyray.load_sound("flap.wav") 
        pyray.set_sound_volume(flap, 0.5)
        
        return flap 
    
    def audio_1():
        """
        Loads sound for game over.
        """
        gameover = pyray.load_sound("over.wav")
    
        return gameover