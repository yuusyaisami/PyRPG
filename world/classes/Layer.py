class Layer:
    def __init__(self):
        self.list = []
    def add(self, obj):
        self.list.append(obj)
    def clear(self, obj):
        self.list = []
    def draw(self, screen):
        for obj in self.list:
            obj.draw(screen)