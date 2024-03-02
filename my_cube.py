from ursina import Entity

class MyCube(Entity):
    def __init__(self, add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self) -> None:
        self.rotation_x += 1
        self.rotation_y += 1
        self.rotation_z += 1
