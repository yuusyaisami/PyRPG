class Graphic:
    def __init__(self):
        self.path = {None: ""}
    def get_path(self, name=None):
        return self.path[name]
    def set_path(self, name, path):
        self.path[name] = path
    