# -*- coding: cp936 -*-
# 创建一个飞船的类,p212

import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        # 加载飞船图像并获取其外接矩形,首先加载图像
        # 获取上面加载图像的属性，图像在屏幕中的属性，既飞船在屏幕中的属性
        # 将表示屏幕的矩形的属性传递给self.screen_sect中，Ship在屏幕中的属性就确定了
        self.image = pygame.image.load('images/ship.bmp') 
        self.rect = self.image.get_rect() 
        self.screen_rect = screen.get_rect() 
        
        # 将每艘新飞船放在屏幕底部中央
        # 飞船中心的x坐标放设置为表示屏幕的矩形属性的centerx
        # 飞船下边缘的y坐标放设置为表示屏幕的矩形属性的bottom
        self.rect.centerx = self.screen_rect.centerx 
        self.rect.bottom = self.screen_rect.bottom
        
        # 在飞船的属性center中存储浮点数值
        self.center = float(self.rect.centerx)
        
        # 移动标志
        self.moving_right = False
        self.moving_left = False
    
    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的center值，而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right: # and左右是两个独立的条件，首先and左边条件为Trut,同时右边小于右边缘才会同时执行，不要理解成and两边都要小于右边缘了
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        # 根据self.center更新rect对象
        self.rect.centerx = self.center
        
    def blitme(self):
        """在指定位置绘制飞船，根据rect属性确定的位置将飞船图像绘制在屏幕中"""
        self.screen.blit(self.image, self.rect)
        
    def center_ship(self):
        """让飞船在屏幕中居中"""
        self.center = self.screen_rect.centerx
