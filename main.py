# 処理はマップ別になっている
# 総合的なグラフィック関連の処理クラスはgraphic.py
# 共有変数はglobal_id.py
import os
import sys
import time
import random
import math
import pygame
windowSize = (800, 600)
def main():
    pygame.init()
    pygame.mixer.pre_init(44100, -16, 2, 4096)
    screen = pygame.display.set_mode(windowSize)
    max_frame_rate = 60
    fps_clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            fps_clock.tick(max_frame_rate)