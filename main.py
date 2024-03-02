from ursina import Ursina

class MyGame:
    def __init__(self) -> None:
        self.app = Ursina()

    def run(self) -> None:
        self.app.run()

if __name__ == '__main__':
    my_game = MyGame()
    my_game.run()