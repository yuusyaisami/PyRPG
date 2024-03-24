from BaseClasses import CharBase, ObjBase, StaticObjBase

class Player(CharBase):
    def __init__(self, x, y, angle, name=None):
        super().__init__(x, y, angle, name)
        self.world_x = 0
        self.world_y = 0
        self.screen_x = 0
        self.screen_y = 0
class OBJ(ObjBase):
    def __init__(self, x, y, angle, name=None):
        super().__init__(x, y, angle, name)
        self.world_x = 0
        self.world_y = 0
        self.screen_x = 0
        self.screen_y = 0
class StaticOBJ(StaticObjBase):
    def __init__(self, x, y, angle, name=None):
        super().__init__(x, y, angle, name)
        self.world_x = 0
        self.world_y = 0
        self.screen_x = 0
        self.screen_y = 0