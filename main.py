from ursina import Ursina, Sky
from snake_head import SnakeHead
from apple import Apple
from random import randint

class MyGame:
    def __init__(self) -> None:
        self.app = Ursina()

    '''
    def add_ground(self) -> None:
        self.ground = Entity(
            model = 'plane', 
            scale = 64, 
            texture = 'grass', 
            texture_scale = (4,4)
        )
    '''

    def add_apples(self):
        number_of_apples = 25
        list_of_apples = []
        for _ in range(number_of_apples):
            i = randint(0, number_of_apples - 1)
            j = randint(0, number_of_apples - 1)
            k = randint(0, number_of_apples - 1)
            list_of_apples.append(Apple(x=i*2, y=j*2, z=k*2))
        return list_of_apples

    def run(self) -> None:
        many_apples = self.add_apples()
        snake_head = SnakeHead(many_apples=many_apples)
        #self.add_ground() # no longer need - have array of cubes # not seeing - possible camera error
        Sky()
        self.app.run()

if __name__ == '__main__':
    my_game = MyGame()
    my_game.run()

# x=i, y=j, z=k, 
#model="sphere", texture="grass"