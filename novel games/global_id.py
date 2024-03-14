class GraphicPathStruct:
    def __init__(self, up_path=None, down_path=None, left_path=None, right_path=None):
        self.up_path = []
        self.down_path = []
        self.left_path = []
        self.right_path = []

        self.up_path.append(up_path)
        self.down_path.append(down_path)
        self.left_path.append(left_path)
        self.right_path.append(right_path)
    def set(self,up_path, down_path, left_path, right_path, animation_id = 0, )
graphicPathsById = []
graphicPathsById.append(GraphicPathStruct(up="GraphicPath/sub1_up.png", down="GraphicPath/sub1_down.png", left="GraphicPath/sub1_left.png", right_path="GraphicPath/sub1_right.png"))
