from ursina import Entity
from ursina import held_keys, time
from ursina import camera
from game_object import GameObject

class SnakeHead(GameObject):
    def __init__(self, add_to_scene_entities=True, **kwargs):
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
        self.z = -1
        self.camera_pivot = Entity(parent=self)
        # configure the camera
        camera.parent = self.camera_pivot # lock camera to head object
        camera.position = (0,0,0)
        camera.rotation = (0,0,0)
        camera.fov = 90

    def cardinalise(self, angle) -> int:
        angle = round(angle, 0)
        cardinal_point = angle%90
        if cardinal_point > 3:
            cardinal_point -= 4
        return cardinal_point * 90

    def update(self) -> None:
        # need to replace with movement from FirstPersonController
        if self.rotation_dx == 0 and self.rotation_dy == 0:
            self.rotation_dx = held_keys[self.turn_down] - held_keys[self.turn_up]
            self.rotation_dy = held_keys[self.turn_right] - held_keys[self.turn_left]
            self.rotation_step = 90
        else:
            self.rotation_x += (self.rotation_dx * time.dt * self.rotation_speed)
            self.rotation_y += (self.rotation_dy * time.dt * self.rotation_speed)
            self.rotation_step -= round(abs((self.rotation_dx - self.rotation_dy) * time.dt * self.rotation_speed), 0)
            print(f'{self.rotation_step=}, {self.rotation_dx=}, {self.rotation_dy=}')
            if self.rotation_step == 0: # reset
                self.rotation_x = self.cardinalise(self.rotation_x)
                self.rotation_y = self.cardinalise(self.rotation_y)
                self.rotation_dx = 0
                self.rotation_dy = 0

        #self.rotation_z += (
        #    (held_keys[self.turn_right] - held_keys[self.turn_left]) 
        #    * time.dt * 100)
        '''
        # update our position in 2D
        self.direction = Vec3(
            self.forward * (
                held_keys[self.controls['forward']] - held_keys[self.controls['backward']]
                )
            + self.right * (
                held_keys[self.controls['right']] - held_keys[self.controls['left']]
                )
            ).normalized()
        # stops you running into things
        # feet_ray = raycast(self.position+Vec3(0,0.5,0), self.direction, traverse_target=self.traverse_target, ignore=self.ignore_list, distance=.5, debug=False)
        head_ray = raycast(self.position+Vec3(0,self.height-.1,0), self.direction, traverse_target=self.traverse_target, ignore=self.ignore_list, distance=.5, debug=False)
        if not head_ray.hit:
            move_amount = self.direction * time.dt * self.speed
            if raycast(self.position+Vec3(-.0,1,0), Vec3(1,0,0), distance=.5, traverse_target=self.traverse_target, ignore=self.ignore_list).hit:
                move_amount[0] = min(move_amount[0], 0)
            if raycast(self.position+Vec3(-.0,1,0), Vec3(-1,0,0), distance=.5, traverse_target=self.traverse_target, ignore=self.ignore_list).hit:
                move_amount[0] = max(move_amount[0], 0)
            if raycast(self.position+Vec3(-.0,1,0), Vec3(0,0,1), distance=.5, traverse_target=self.traverse_target, ignore=self.ignore_list).hit:
                move_amount[2] = min(move_amount[2], 0)
            if raycast(self.position+Vec3(-.0,1,0), Vec3(0,0,-1), distance=.5, traverse_target=self.traverse_target, ignore=self.ignore_list).hit:
                move_amount[2] = max(move_amount[2], 0)
            self.position += move_amount # think this is simple 2D movement
            # self.position += self.direction * self.speed * time.dt
        '''