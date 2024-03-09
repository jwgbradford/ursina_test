from ursina import Entity
from utils import load_kwargs

class GameObject(Entity):
    def __init__(self, add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs)
        settings = load_kwargs("sphere_settings.json")
        for key, value in settings.items():
            setattr(self, key, value)
        # custom object kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self) -> None:
        pass