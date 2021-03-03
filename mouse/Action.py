import pyautogui
from random import randint
from pygame import mixer
import time

from mouse.Voice import Voice


class Action(Voice):
    def __init__(self, screen_width: int = 960, screen_height: int = 540, voice_mode: str = 'en'):
        super().__init__(voice_mode)
        self.__speed: float = 0.1
        self.__screen_width: int = screen_width
        self.__screen_height: int = screen_height
        self.__voice: Voice = Voice(voice_mode)
        pyautogui.FAILSAFE = False

    def _start_action(self) -> None:
        print('run')
        self.__voice._launch()
        time.sleep(0.3)
        self.__voice._start()

    def _confused_action(self) -> None:
        self.__voice._confused()

    def _fast_move_x(self, controller: object, x_position: int = 960, y_position: int = 540) -> None:
        """
        make to the __mouse fast and random direction
        :return:
        """
        self.__voice._move_fast_x()
        confused = randint(1, 100)
        while mixer.music.get_busy():
            pyautogui.moveTo(x=randint(0, self.__screen_width), y=randint(0, self.__screen_height),
                             duration=self.__speed)
        if confused < 26:
            controller.position = (x_position, y_position)
            self._confused_action()

    def _slow_move_x(self):
        speak = randint(1, 100)
        if speak <= 10:
            self.__voice._move_slow_x()

    def _medium_move_x(self):
        speak = randint(1, 100)
        if speak <= 10:
            self.__voice._medium_move_x()

    def _first_move_action(self, started, axes_difference) -> bool:
        if not started and axes_difference > 60:
            self.__voice._first_move()
            return True
