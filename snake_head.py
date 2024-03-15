from ursina import Entity
from ursina import time
from ursina import camera
from game_object import GameObject
from utils import load_kwargs

class SnakeHead(GameObject):
    def __init__(self, add_to_scene_entities=True, **kwargs) -> None:
        super().__init__(add_to_scene_entities, **kwargs)
        settings = load_kwargs("head_settings.json")
        for key, value in settings.items():
            setattr(self, key, value)
        # configure the camera
        self.camera_pivot = Entity(parent=self)
        camera.parent = self.camera_pivot # lock camera to head object
        camera.position = (1, 1, -10)
        camera.rotation = (0,0,0)
        #camera.fov = 90

    def cardinalise(self, angle:float=0) -> int:
        if angle < 0: # be wary of -ve values
            angle += 360
        cardinal_point = round(angle / 90, 0)
        if cardinal_point > 3:
            cardinal_point = 0
        return cardinal_point * 90

    def input(self, key) -> None:
        if self.rotation_step == 0: # we're not already in a turn
            match key:
                case self.turn_left:
                    self.rotation_dy = -1
                case self.turn_right:
                    self.rotation_dy = 1
                case self.turn_up:
                    self.rotation_dx = -1
                case self.turn_down:
                    self.rotation_dx = 1
            if self.rotation_dx ^ self.rotation_dy:
                self.rotation_step = 90

    def reset_rotation(self) -> None:
            self.rotation_step = 0
            self.rotation_dx = 0
            self.rotation_dy = 0
            self.rotation_x = self.cardinalise(self.rotation_x)
            self.rotation_y = self.cardinalise(self.rotation_y)

    def recenter_position(self) -> None:
        self.x = round(self.x, 0)
        self.y = round(self.y, 0)
        self.z = round(self.z, 0)

    def update(self) -> None:
        if self.motion_step > 0: # not turning, move forward
            self.position += self.forward * time.dt * self.motion_speed
            self.motion_step -= time.dt * self.motion_speed
        elif self.rotation_step > 0: # start turn at end of next move
            self.rotation_x += (self.rotation_dx * time.dt * self.rotation_speed)
            self.rotation_y += (self.rotation_dy * time.dt * self.rotation_speed)
            self.rotation_step -= time.dt * self.rotation_speed
            if self.rotation_step < 0: # reset turn to zero
                self.reset_rotation()
                self.recenter_position()
        elif self.motion_step < 0: # finished turning / moving, move again
            self.motion_step = 2
            self.recenter_position()
        '''
        for ball in self.many_balls:
            if self.intersects(ball).hit:
                print('player is inside trigger box')
        '''