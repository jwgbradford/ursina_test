from ursina import Entity
from ursina import held_keys, time

class MyCube(Entity):
    def __init__(self, add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self) -> None:
        self.rotation_x += (
            (held_keys[self.controls['up']] - held_keys[self.controls['down']]) 
            * time.dt * 100)
        #self.rotation_y += 1
        self.rotation_z += (
            (held_keys[self.controls['left']] - held_keys[self.controls['right']]) 
            * time.dt * 100)
