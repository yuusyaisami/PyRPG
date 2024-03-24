class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Angle:
    def __init__(self, angle):
        self.value = angle
class ObjBase: # マップの動的クラス マップの移動は不可能
    def __init__(self, type, graphic_id, graphic_name):
        self.type = type
        self.graphic_id = graphic_id
        self.graphic_name = graphic_name
        