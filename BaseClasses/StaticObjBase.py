class StaticObjBase: # マップの静的オブジェクトクラス
    def __init__(self, type, graphic_id=-1, graphic_name=None):
        self.type = type
        self.graphic_id = graphic_id
        self.graphic_name = graphic_name