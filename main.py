from ursina import Ursina, Entity
from ursina import color
from my_cube import MyCube
from json import load

class MyGame:
    def __init__(self) -> None:
        self.app = Ursina()

    def load_kwargs(self) -> dict:
        with open("cube_settings.json") as input_file:
            dict_data = load(input_file)
        return dict_data

    def add_my_block(self) -> None:
        settings = self.load_kwargs()
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
        self.add_ground()
        self.app.run()

if __name__ == '__main__':
    my_game = MyGame()
    my_game.run()