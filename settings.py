"""
@Author:夜寒
@File:settings.py
@Time:2024/5/6 11:11
@Project:aliensinvasion
@IDE:PyCharm
"""


class Settings:
    """存储游戏中所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 1440
        self.screen_height = 900
        self.bg_color = (230, 230, 230)
