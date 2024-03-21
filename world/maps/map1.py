from graphic_classes.graphic import GraphicBuffer
from world.classes.Layer import Layer
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1,],
    [1, 0, 0, 0, 0, 0, 0, 0, 1,],
    [1, 0, 0, 0, 0, 0, 0, 0, 1,],
    [1, 1, 0, 1, 1, 0, 0, 0, 1,],
    [1, 0, 0, 0, 0, 0, 1, 1, 1,],
    [1, 1, 0, 1, 1, 0, 0, 0, 1,],
    [1, 0, 0, 0, 0, 0, 0, 0, 1,],
    [1, 1, 1, 1, 1, 1, 1, 1, 1,]
]

class Map:
    def __init__(self):
        self.map = mini_map
        self.worldPos = (100, 100)
        self.buffer = GraphicBuffer()
        self.layer = Layer()
        self.buffer.add(1, 0)
        self.buffer.add(2, 0)

    def draw(self):
        