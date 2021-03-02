import pyautogui

from random import randint


class Action:
    def __init__(self):
        self.__speed = 0.1
        pyautogui.FAILSAFE = False


    def _fast_movement_random(self, screen_width: int = 0, screen_height: int = 0, time: float = 1):
        """
        make to the __mouse fast and random direction
        :return:
        """
        while time > float(0):
            pyautogui.moveTo(x=randint(0, screen_width), y=randint(0, screen_height), duration=self.__speed)
            time -= self.__speed
