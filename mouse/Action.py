import pyautogui


class Action:
    def __init__(self):
        self.__speed = 0.5
        pyautogui.FAILSAFE = False

    def fast_movement_random(self):
        """
        make to the mouse fast and random direction
        :return:
        """
        pyautogui.moveTo(x=200, y=300, duration=self.__speed)