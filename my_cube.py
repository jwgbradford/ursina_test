from ursina import Entity
from ursina import held_keys, time
from ursina import camera

class MyCube(Entity):
    def __init__(self, add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs)
        # default aswd controls
        self.turn_up = 'w'
        self.turn_down = 's'
        self.turn_right = 'd'
        self.turn_left = 'a'
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.camera_pivot = Entity(parent=self, z=-2)
        # configure the camera
        camera.parent = self.camera_pivot
        camera.position = (0,0,0)
        camera.rotation = (0,0,0)
        camera.fov = 90

    def update(self) -> None:
        self.rotation_x += (
            (held_keys[self.turn_down] - held_keys[self.turn_up]) 
            * time.dt * 100)
        self.rotation_y += (
            (held_keys[self.turn_right] - held_keys[self.turn_left]) 
            * time.dt * 100)
        #self.rotation_z += (
        #    (held_keys[self.turn_right] - held_keys[self.turn_left]) 
        #    * time.dt * 100)
