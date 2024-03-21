import math
# entityすべてがこのクラスを持つ BaseClassです
# 数値の指定は関数にて行う
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Angle:
    def __init__(self, angle):
        self.value = angle
    def get(self):
        """Returns the angle in string"""
        if self.value == 0:
            return "up"
        if self.value == 90:
            return "right"
        if self.value == 180:
            return "down"
        if self.value == 270:
            return "left"
        else:
            return str(self.value)

class CharBase:
    def __init__(self, x, y, angle, name=None):
        self.world_pos = Position(x, y) # world position
        self.screen_pos = Position(0, 0) # draw時に入力する
        self.float_pos = Position(0, 0) # float position
        self.size = 1
        self.angle = Angle(angle)
        self.stute = "idol" # キャラクターの状態を入力 idol:通常, dead:死んでいる,None :何もない, move:移動中, attack:攻撃中
        self.name = name # キャラクターの名前
        self.hp = 100 # HP
        self.mp = 100 # MP
        self.speed = 0.1 # 移動スピード
    def getPosIndex(self, world_size_x):
        """Returns the index of the position."""
        return self.world_pos.x + self.world_pos.y * world_size_x
    def move(self, map, entities, angle=-1):
        """
        Moves the character on the map in the direction of the given angle.

        Parameters
        ----------
        map : list of list of Block
            The map of the game world.
        entities : list of Entity
            The list of entities in the game world.
        angle : int, optional
            The angle of the movement, in degrees. If not specified, the current
            angle of the character is used.

        Returns
        -------
        None

        """
        if angle != -1: # -1以外なら角度を入力する
            self.angle.value = angle
        tmpx = self.world_pos.x # 壁との衝突を検知したら戻す
        tmpy = self.world_pos.y

        self.float_pos.y += math.cos(self.angle.value) * self.speed
        self.float_pos.x += math.sin(self.angle.value) * self.speed # 移動した分の座標を入れる

        
        
        if not self.__collision_block(map, tmpx, tmpy): # 第一関門　マップとの衝突検知 しなかったらentity検知へ
            px = self.float_pos.x
            py = self.float_pos.y
            for entity in entities: # 第二関門　エンティティとの衝突検知 衝突したらifを抜ける
                x, y, s = entity.getPosFloat() # すべてのentityはこのクラスを持つ
                flag_px = (px > x and px < x + s)
                flag_py = (py > y and py < y + s)
                flag_px_s = (px + s > x and px + s < x + s)
                flag_py_s = (py + s > y and py + s < y + s)
                flag_collision = ((flag_px and flag_py) or (flag_px_s and flag_py) or (flag_px and flag_py_s) or (flag_px_s and flag_py_s))
                if not flag_collision:
                    self.world_pos.x = int(self.float_pos.x)
                    return # 衝突しなかった 
        # 衝突した
        self.float_pos.y = tmpy
        self.float_pos.x = tmpx
    def __collision_block(self, map, tx, ty):
        if self.angle.value > 0 and self.angle.value < 90:
            flag_up_left = map[int(self.float_pos.y)][self.float_pos.x].type != "wall"
            flag_up_right = map[int(self.float_pos.y)][int(self.float_pos.x) + self.size].type != "wall"
            flag_down_right = map[int(self.float_pos.y) + self.size][int(self.float_pos.x)].type != "wall"
            if flag_up_left and flag_up_right and not flag_down_right:
                self.float_pos.x = tx
                self.angle = 90
            elif flag_up_right and flag_down_right and not flag_up_left:
                self.float_pos.y = ty
                self.angle = 0
            elif flag_up_left or flag_down_right or flag_up_right:
                flag_collision_block = True
            else:
                pass # 問題なし no collision
        elif self.angle.value > 90 and self.angle.value < 180:
            flag_up_right = map[int(self.float_pos.y)][int(self.float_pos.x + self.size)].type != "wall"
            flag_down_right = map[int(self.float_pos.y) + self.size][int(self.float_pos.x) + self.size].type != "wall"
            flag_down_left = map[int(self.float_pos.y) + self.size][int(self.float_pos.x)].type != "wall"
            if flag_up_right and flag_down_right and not flag_down_left:
                self.float_pos.x = tx
                self.angle = 180
            elif flag_down_left and flag_down_right and not flag_up_right:
                self.float_pos.y = ty
                self.angle = 90
            elif flag_up_right or flag_down_left or flag_down_right:
                flag_collision_block = True
            else:
                pass # 問題なし no collision
        elif self.angle.value > 180 and self.angle.value < 270:
            flag_down_right = map[int(self.float_pos.y) + self.size][int(self.float_pos.x) + self.size].type != "wall"
            flag_down_left = map[int(self.float_pos.y) + self.size][int(self.float_pos.x)].type != "wall"
            flag_up_left = map[int(self.float_pos.y)][int(self.float_pos.x)].type != "wall"
            if flag_down_right and flag_down_left and not flag_up_left:
                self.float_pos.x = tx
                self.angle = 270
            elif flag_up_left and flag_down_left and not flag_down_right:
                self.float_pos.y = ty
                self.angle = 180
            elif flag_down_right or flag_up_left or flag_down_left:
                flag_collision_block = True
            else:
                pass # 問題なし no collision
        elif self.angle.value > 270 and self.angle.value < 360:
            flag_down_left = map[int(self.float_pos.y) + self.size][int(self.float_pos.x)].type != "wall"
            flag_up_left = map[int(self.float_pos.y)][int(self.float_pos.x)].type != "wall"
            flag_up_right = map[int(self.float_pos.y)][int(self.float_pos.x) + self.size].type != "wall"
            if flag_down_left and flag_up_left and not flag_up_right:
                self.float_pos.x = tx
                self.angle = 0
            elif flag_up_right and flag_up_left and not flag_down_left:
                self.float_pos.y = ty
                self.angle = 270
            elif flag_down_left or flag_up_right or flag_up_left:
                flag_collision_block = True
            else:
                pass # 問題なし no collision
        elif self.angle.value == 0:
            flag_up_left = map[int(self.float_pos.y)][self.float_pos.x].type != "wall"
            flag_up_right = map[int(self.float_pos.y)][int(self.float_pos.x) + self.size].type != "wall"
            if flag_up_left or flag_up_right:
                flag_collision_block = True
            else:
                pass # 問題なし no collision
        elif self.angle.value == 90:
            flag_up_right = map[int(self.float_pos.y)][int(self.float_pos.x) + self.size].type != "wall"
            flag_down_right = map[int(self.float_pos.y) + self.size][int(self.float_pos.x) + self.size].type != "wall"
            if flag_up_right or flag_down_right:
                flag_collision_block = True
            else:
                pass # 問題なし no collision
        elif self.angle.value == 180:
            flag_down_right = map[int(self.float_pos.y) + self.size][int(self.float_pos.x) + self.size].type != "wall"
            flag_down_left = map[int(self.float_pos.y) + self.size][int(self.float_pos.x)].type != "wall"
            if flag_down_right or flag_down_left:
                flag_collision_block = True
            else:
                pass # 問題なし no collision
        elif self.angle.value == 270:
            flag_up_left = map[int(self.float_pos.y)][int(self.float_pos.x)].type != "wall"
            flag_down_left = map[int(self.float_pos.y) + self.size][int(self.float_pos.x)].type != "wall"
            if flag_up_left or flag_down_left:
                flag_collision_block = True
            else:
                pass # 問題なし no collision
        else:
            print(" エラー : 角度が不正です ")
            pass # エラー
        if flag_collision_block:
            return True
        return False
    def move_to_block(self, map, entities, angle=-1):
        if angle != -1: # -1以外なら角度を入力する
            self.angle.value = angle
        
    def getPosFloat(self):
        """Returns the float position and size."""
        return self.float_pos.x, self.float_pos.y, self.size 