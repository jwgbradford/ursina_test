from ursina import Ursina, Entity, Sky, Vec3
from snake_head import SnakeHead
from game_object import GameObject
from utils import load_kwargs

class MyGame:
    def __init__(self) -> None:
        self.app = Ursina()

    def add_my_block(self) -> None:
        settings = load_kwargs("cube_settings.json")
        self.my_block = SnakeHead(**settings)

    def add_ground(self) -> None:
        self.ground = Entity(
            model = 'plane', 
            scale = 64, 
            texture = 'grass', 
            texture_scale = (4,4)
        )

    def add_balls(self) -> list[list[list[Entity]]]:
        settings = load_kwargs("sphere_settings.json")
        array_size = 10
        array_of_balls = []
        for i in range(array_size):
            plane_of_balls = []
            for j in range(array_size):
                row_of_balls = []
                for k in range(array_size):
                    row_of_balls.append(GameObject(x=i*2, y=j*2, z=k*2, **settings))
                plane_of_balls.append(row_of_balls)
            array_of_balls.append(plane_of_balls)
        return array_of_balls


    def run(self) -> None:
        self.add_my_block()
        #self.add_ground() # no longer need - have array of cubes # not seeing - possible camera error
        self.many_balls = self.add_balls()
        Sky()
        self.app.run()

if __name__ == '__main__':
    my_game = MyGame()
    my_game.run()

# x=i, y=j, z=k, 
#model="sphere", texture="grass"