from utils.math.vector import Vector2

class Entity:
    def __init__(self):
        self.position = Vector2()
        self.name = None
        self.color = None
        self.visible = True
        self.image = None
        self.sprites = None

    def render(self, screen):
        pass

    def update(self, dt):
        pass

    def setPosition(self):
        pass

    def reset(self):
        pass

    pass