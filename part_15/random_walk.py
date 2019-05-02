# -*- coding: cp936 -*-
# 详细见P296
# 随机漫步

from random import choice

class RandomWalk():
    """一个生成随机漫步的类"""
    
    def __init__(self, num_points=50):
        """初始化随机漫步的属性"""
        self.num_points = num_points
        
        # 所有随机漫步都是始于（0,0）
        self.x_values = [0]
        self.y_values = [0]
        
    def fill_walk(self):
        """计算随机漫步包含的所有的点"""
        
        # 不断漫步，直到列表到达指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7])
            x_step = x_direction * x_distance
            
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7])
            y_step = y_direction * y_distance
            
            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            
            # 计算下一个点的x和y值,切片[-1]为列表的最后一个值，
            # 初始点是（0,0），第一次循环x走2，y走3，就是0+2,0+3
            # 得到第二个点（2,3）
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            # 将每次得到一个点的x,y坐标加入到列表中
            self.x_values.append(next_x)
            self.y_values.append(next_y)
        

            

