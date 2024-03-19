from classes.Animation import Animation
from classes.Camera import Camera
from classes.Collider import Collider
from entities.EntityBase import EntityBase
class Player(EntityBase):
    def __init__(self):
        self.world_x = 0
        self.world_y = 0
        self.screen_x = 0
        self.screen_y = 0

        self.camera = Camera()
        self.animation = Animation()
        self.Collider = Collider()
    def getPosIndex(self):
        return self.world_x / 32, self.world_y / 32
    def setPosIndex(self, x, y):