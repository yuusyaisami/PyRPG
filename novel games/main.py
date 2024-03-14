import os
import sys
import time
import random
import math
import pygame
import graphic
global_id = graphic.global_id

class Map:
    def __init__(self):
        self.main_map = [] # メインで使われるマップ
        self.back_map = [] # バックグラウンドで使われるマップ
        self.width = 0 #　スクリーンでの合計した、横の長さ
        self.height = 0
        self.tile_width = 0 # タイルの個数
        self.tile_height = 0
    