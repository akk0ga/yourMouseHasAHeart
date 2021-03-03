import pyautogui

from random import randint
from pygame import mixer
from win32api import GetSystemMetrics as screen_size


class Action:
    def __init__(self):
        self.__speed = 0.1
        self.__screen_width = screen_size(0)
        self.__screen_height = screen_size(1)
        pyautogui.FAILSAFE = False

    def _fast_movement_random(self, screen_width: int = 0, screen_height: int = 0):
        """
        make to the __mouse fast and random direction
        :return:
        """
        while mixer.music.get_busy():
            pyautogui.moveTo(x=randint(0, self.__screen_width), y=randint(0, self.__screen_height),
                             duration=self.__speed)
