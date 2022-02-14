#from typing_extensions import Self

import pytest
import pyray 
from pyray import Texture

from main import check_collide
from game.score.score import display_score
from game.pipe.pipe import Obstacle, Bottom
from game.picture.pictures import Pictures

#from main
def test_check_collide():
    """making sure the collide is returning a bool"""
    cc = check_collide()
    assert isinstance(cc, bool) 

#from score
def test_display_score():
    game_over = True
    assert display_score(game_over, 0) == None


# I don't think we need this test. - Emilee
#from pictures
#def test_pipes():
    #"""Checking if image overlay for pipes is a texture"""
    #p = Pictures()
    #pipe_1 = p.pipe_1()
    #assert isinstance(pipe_1, Texture)
    
    #pipe_2 = p.pipe_2()
    #assert pipe_2 == Texture




# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])