from ursina import Ursina, Entity
from ursina import color

class MyGame:
    def __init__(self) -> None:
        self.app = Ursina()

    def add_my_block(self) -> None:
        self.my_block = Entity(
            model = 'cube', 
            color = color.orange, 
            texture = 'brick', 
            rotation=(45,0,45)
        )

    def run(self) -> None:
        self.add_my_block()
        self.app.run()

if __name__ == '__main__':
    my_game = MyGame()
    my_game.run()