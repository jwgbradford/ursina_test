from ursina import Entity

class MySphere(Entity):
    def __init__(self, add_to_scene_entities=True, **kwargs):
        super().__init__(add_to_scene_entities, **kwargs)
        # default aswd controls
        for key, value in kwargs.items():
            setattr(self, key, value)

    def update(self) -> None:
        pass