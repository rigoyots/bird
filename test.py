"""Run this file like you would 'main' """

import pytest
import pyray 
from pyray import Texture

from main import check_collide
from game.score.score import display_score
from game.pipe.pipe import Obstacle, Bottom
from game.picture.pictures import Pictures
import game.Bird.bird

#from main
def test_check_collide():
    """making sure the collide is returning a bool"""
    cc = check_collide()
    assert isinstance(cc, bool) 

#from score
def test_display_score():
    """Tests:
        display_score()"""
    game_over = True
    assert display_score(game_over, 0) == None


def test_movebird(monkeypatch):
    """
    Tests: 
        move_bird()

    Functions:
        mock_is_key_pressed(x)
        mock_get_frame_time()
    """
    def mock_is_key_pressed(x):
        return True

    def mock_get_frame_time():
        return 1

    monkeypatch.setattr("game.Bird.bird.IsKeyPressed", mock_is_key_pressed)
    monkeypatch.setattr("game.Bird.bird.GetFrameTime", mock_get_frame_time)
    b = game.Bird.bird.Bird(500, 500, 5)
    b.move_bird()
    assert b.y == 500



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])