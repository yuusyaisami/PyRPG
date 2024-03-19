from typing import Any
import paths
import pygame
class GraphicBufferItem: # 読み込んだ画像を保存する場所(二重呼び出しを避けるため)
    def __init__(self, id, angle, paths):
        if angle == 0:
            self.buffer = pygame.image.load(paths.graphicPathsById[id].up_path).convert_alpha() 
        if angle == 90:
            self.buffer = pygame.image.load(paths.graphicPathsById[id].right_path).convert_alpha()
        if angle == 180:
            self.buffer = pygame.image.load(paths.graphicPathsById[id].down_path).convert_alpha()
        if angle == 270:
            self.buffer = pygame.image.load(paths.graphicPathsById[id].left_path).convert_alpha()
        self.buffer = pygame.transform.scale(self.buffer, (32, 32))
        self.id = id
        self.angle = angle
    def compare(self, id, angle):
        if self.id == id and self.angle == angle:
            return True
        else:
            return False
class GraphicBuffer:
    def __init__(self, ):
        self.graphicPathsById = paths.graphicPathsById
        self.buffer_list = []
    def add(self, id: int, angle: int) -> None:
        for i in range(len(self.buffer_list)):
            if self.buffer_list[i].compare(id, angle):
                return  # already added  # すでに追加されている
        self.buffer_list.append(GraphicBufferItem(id, angle))
    def clear(self):
        """Clears the graphic buffer."""
        self.buffer_list = []