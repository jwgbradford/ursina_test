from ursina import Ursina
from ursina import color
from my_cube import MyCube
from json import load

class MyGame:
    def __init__(self) -> None:
        self.app = Ursina()

    def load_kwargs(self, key) -> dict:
        with open("controls.json") as input_file:
            input_data = load(input_file)
        print(input_data)
        dict_data = input_data[key]
        return dict_data

    def add_my_block(self) -> None:
        controls = self.load_kwargs('movement')
        print(controls)
        self.my_block = MyCube(
            model = 'cube', 
            color = color.orange, 
            texture = 'brick', 
            rotation=(45,0,45),
            controls = controls
        )

    def run(self) -> None:
        self.add_my_block()
        self.app.run()

if __name__ == '__main__':
    my_game = MyGame()
    my_game.run()