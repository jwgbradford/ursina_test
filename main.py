from ursina import Ursina, Entity, Sky
from snake_head import SnakeHead
from apple import Apple
from random import randint

class MyGame:
    def __init__(self) -> None:
        self.app = Ursina()

    def add_ground(self) -> None:
        self.ground = Entity(
            model = 'plane', 
            scale = 64, 
            texture = 'grass', 
            texture_scale = (4,4)
        )

    def add_balls(self) -> list[list[list[Entity]]]:
        array_size = 25
        array_of_balls = [
            [[None for _ in range(array_size)
                    ] for _ in range(array_size)
                        ] for _ in range(array_size)
        ]
        for _ in range(array_size):
            i = randint(0, array_size - 1)
            j = randint(0, array_size - 1)
            k = randint(0, array_size - 1)
            array_of_balls[i][j][k] = Apple(x=i*2, y=j*2, z=k*2)
        return array_of_balls

    def run(self) -> None:
        self.snake_head = SnakeHead()
        #self.add_ground() # no longer need - have array of cubes # not seeing - possible camera error
        self.many_balls = self.add_balls()
        Sky()
        self.app.run()

if __name__ == '__main__':
    my_game = MyGame()
    my_game.run()

# x=i, y=j, z=k, 
#model="sphere", texture="grass"