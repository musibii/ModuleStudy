# -*- coding: utf-8 -*-
# __author__: musibii
# __file__  : 八大行星动画演示.py
# __time__  : 2020/6/17 2:51 下午


"""一个简单的演示八大行星公转的动画，采用arcade街机游戏模块制作，安装Arcade请用pip install arcade --user。
A simple animation to simulate the rotation of eight planets is made by using Arcade module. To install Arcade, use PIP install arcade--user.
"""

__author__ = "lixingqiu"
__date__ = "2019/3/8"

import time
import math
import arcade
import random

SCREEN_WIDTH = 1350
SCREEN_HEIGHT = 780
SCREEN_TITLE = "eight planet 八大行星"


class Planet(arcade.Sprite):
    def __init__(self, image, a, b, angle, speed):
        """image:造型图片,a：Long axis长半轴，b：semi-minor axis短半轴，angle：初始角度"""
        super().__init__(image)
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.direction = angle  # 自定义direction，不用原有属性angle
        self.a = a
        self.b = b
        self.speed = speed

    def update(self):
        """ Calculating Initial Coordinates Based on Elliptic Parametric Equation"""

        self.direction = self.direction + 365 / self.speed
        self.direction = self.direction % 360
        x = SCREEN_WIDTH / 2 + self.a * math.cos(math.radians(self.direction))  # 根据椭圆参数方程算起始坐标
        y = SCREEN_HEIGHT / 2 + self.b * math.sin(math.radians(self.direction))
        self.center_x = x
        self.center_y = y
        super().update()


class MyGame(arcade.Window):
    """
    继承自窗口的MyGame类.
    """

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)

    def setup(self):
        """ 这里是对游戏中的各个对象进行设置 """

        self.planet_list = arcade.SpriteList()  # 新建角色列表，以便统一渲染

        # 背景角色生成
        pass

        # 太阳角色生成
        pass

        # 行星角色生成
        pass

        for i in range(8):  # 生成8个行星
            angle = self.angle_list[i]
            a, b = self.ab_list[i]
            image = self.planets_image[i]
            speed = self.days[i]
            aplanet = Planet(image, a, b, angle, speed)  # 新建行星
            self.planet_list.append(aplanet)  # 添加到所有行星列表

    def update(self, x):
        """每帧更新游戏内在逻辑"""

        self.planet_list.update()
        self.sun.update_animation()

    def on_draw(self):
        """渲染屏幕 """

        arcade.start_render()

        # 开始画背景
        self.background.draw()
        self.sun.draw()
        self.planet_list.draw()


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
