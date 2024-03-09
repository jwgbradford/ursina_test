from ursina import Entity
from ursina import time
from ursina import camera
from game_object import GameObject

class SnakeHead(GameObject):
    def __init__(self, add_to_scene_entities=True, **kwargs) -> None:
        super().__init__(add_to_scene_entities, **kwargs)
        # default aswd controls
        self.turn_up = 'w'
        self.turn_down = 's'
        self.turn_right = 'd'
        self.turn_left = 'a'
        self.rotation_dx = 0 # our turn controller
        self.rotation_dy = 0
        self.rotation_step = 0
        self.rotation_speed = 100
        for key, value in kwargs.items():
            setattr(self, key, value)
        # configure the camera
        self.camera_pivot = Entity(parent=self)
        camera.parent = self.camera_pivot # lock camera to head object
        camera.position = (0,0,0)
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
        if self.rotation_step == 0: #we're not alredy in a turn
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

    def update(self) -> None:
        # haven't decided on a motion method yet
        if self.rotation_step == 0: # not turning, move forward
            self.position += self.forward * time.dt * 2
        #self.animate_position(self.position + self.forward, duration=0.5)
        #self.animate('position', self.forward, duration=0.5)
        '''
        should start rotation on arrow keypress, then continue until 90
        should then stop and centre on either 0, 90, 180, 270
        '''
        if self.rotation_dx ^ self.rotation_dy:
            self.rotation_x += (self.rotation_dx * time.dt * self.rotation_speed)
            self.rotation_y += (self.rotation_dy * time.dt * self.rotation_speed)
            self.rotation_step -= time.dt * self.rotation_speed
            if self.rotation_step < 0: # reset
                self.reset_rotation()
