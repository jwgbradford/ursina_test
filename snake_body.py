from game_object import GameObject
from ursina import time

class SnakeBody(GameObject):
    def __init__(self, add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs)