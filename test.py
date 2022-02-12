import pytest
import pyray

from main import check_collide
from game.score.score import display_score
from game.pipe.pipe import obstacle, bottom

#from main
def test_check_collide():
    """making sure the collide is returning a bool"""
    cc = check_collide()
    assert isinstance(cc, bool) 

#from score
def test_display_score():
    game_over = True
    assert display_score(game_over, 0) != True









# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])