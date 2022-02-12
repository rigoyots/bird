# Emilee's Tests - bird.py

import pytest
import game.Bird.bird

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
    assert b.y == -100

