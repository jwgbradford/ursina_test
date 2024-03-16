from my_objects.game_object import GameObject
from utils import load_kwargs

class SnakeBody(GameObject):
    def __init__(self, add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs)
        settings = load_kwargs("body_settings.json")
        for key, value in settings.items():
            setattr(self, key, value)