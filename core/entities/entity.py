from utils.math.vector import Vector2

class Entity:
    def __init__(self):
        self.position = Vector2()
        self.name = None
        self.color = None
        self.image = None
        self.sprites = None
        self.visible = True
        # self.active = True

    def render(self, screen):
        pass

    def update(self, dt):
        pass

    def setPosition(self):
        pass

    def reset(self):
        pass

    def show(self):
        self.visible = True
    
    def hide(self):
        self.visible = False

    # def enable(self):
    #     self.active = True
    
    # def disable(self):
    #     self.active = False
    pass