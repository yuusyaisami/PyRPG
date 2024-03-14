from typing import Any
import global_id as gid
import pygame
global_id = gid
class GraphicBufferItem: # 読み込んだ画像を保存する場所(二重呼び出しを避けるため)
    def __init__(self, id, angle):
        self.graphic_buffer = pygame.image.load(global_id.graphicPathsById[id].up_path).convert_alpha() 
        self.graphic_buffer = pygame.transform.scale(self.graphic_buffer, (32, 32))
        self.graphic_buffer_id = id
        self.graphic_buffer_angle = angle
    def compare(self, id, angle):
        if self.graphic_buffer_id == id and self.graphic_buffer_angle == angle:
            return True
        else:
            return False
class GraphicBuffer:
    def __init__(self):
        self.graphic_buffer_list = []
    def add(self, id: int, angle: int) -> None:
        for i in range(len(self.graphic_buffer_list)):
            if self.graphic_buffer_list[i].compare(id, angle):
                return  # already added  # すでに追加されている
        self.graphic_buffer_list.append(GraphicBufferItem(id, angle))
    def clear(self):
        """Clears the graphic buffer."""
        self.graphic_buffer_list = []
class MapItem:
    def __init__(self, id, name, angle):
        self.id = id
        self.name = name
        self.graphic = None
        self.angle = angle

        
    def set_graphic(self, animation_id=0):
        if self.angle == 0:
            self.graphic = global_id.graphicPathsById[self.id].up_path[int(animation_id)]
        if self.angle == 90:
            self.graphic = global_id.graphicPathsById[self.id].right_path[int(animation_id)]
        if self.angle == 180:
            self.graphic = global_id.graphicPathsById[self.id].down_path[int(animation_id)]
        if self.angle == 270:
            self.graphic = global_id.graphicPathsById[self.id].left_path[int(animation_id)]