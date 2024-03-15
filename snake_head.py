from ursina import Entity
from ursina import time, destroy
from ursina import camera
from game_object import GameObject
from apple import Apple
from utils import load_kwargs
from random import randint

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

    def move_turn(self) -> None:
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

    def eat_apple(self):
        # need to removed collided apples, and add new one
        apple_to_remove = -1
        for i, apple in enumerate(self.many_apples):
            if self.intersects(apple).hit:
                apple_to_remove = i
                print('player is inside trigger box')
        if apple_to_remove > -1:
            # remove eaten apple from list and destroy entity
            eaten_apple = self.many_apples.pop(apple_to_remove)
            destroy(eaten_apple)
            # add a new apple to the playing area
            number_of_apples = 25
            i = randint(0, number_of_apples - 1)
            j = randint(0, number_of_apples - 1)
            k = randint(0, number_of_apples - 1)
            self.many_apples.append(Apple(x=i*2, y=j*2, z=k*2))

    def update(self) -> None:
        self.move_turn()
        self.eat_apple()