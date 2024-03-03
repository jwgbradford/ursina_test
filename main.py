from ursina import Ursina, Entity, Sky
from my_cube import MyCube
from utils import load_kwargs

class MyGame:
    def __init__(self) -> None:
        self.app = Ursina()

    def add_my_block(self) -> None:
        settings = load_kwargs("cube_settings.json")
        self.my_block = MyCube(**settings)

    def add_ground(self) -> None:
        self.ground = Entity(
            model = 'plane', 
            scale = 64, 
            texture = 'grass', 
            texture_scale = (4,4)
        )

    def run(self) -> None:
        self.add_my_block()
        self.add_ground() # not seeing - possible camera error
        Sky()
        self.app.run()

if __name__ == '__main__':
    my_game = MyGame()
    my_game.run()