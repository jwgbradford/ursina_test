from ursina import Ursina, Entity
from ursina import color

class MyGame:
    def __init__(self) -> None:
        self.app = Ursina()

    def add_entities(self) -> None:
        self.my_ball = Entity(model = 'quad', color = color.orange, texture = 'brick')


    def run(self) -> None:
        self.add_entities()
        self.app.run()

if __name__ == '__main__':
    my_game = MyGame()
    my_game.run()