class GraphicPathStruct:
    def __init__(self, up_path=None, down_path=None, left_path=None, right_path=None):
        self.up_path = []
        self.down_path = []
        self.left_path = []
        self.right_path = []

        self.add(up_path, down_path, left_path, right_path)
    def add(self,up_path, down_path, left_path, right_path,  ):
        self.up_path.append(up_path)
        self.down_path.append(down_path)
        self.left_path.append(left_path)
        self.right_path.append(right_path)
graphicPathsById = []
# グラフィックパスの辞書に登録したい画像をIDとAngleをキーに保存する
graphicPathsById.append(GraphicPathStruct(up="sub1_up.png", down="sub1_down.png", left="sub1_left.png", right_path="sub1_right.png"))
