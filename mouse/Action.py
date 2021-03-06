import pyautogui
from random import randint
from pygame import mixer
import time
from mouse.Voice import Voice


class Action(Voice):
    def __init__(self, controller: object, screen_width: int = 960, screen_height: int = 540, voice_mode: str = 'en'):
        super().__init__(voice_mode)
        self.__speed: float = 0.1
        self.__screen_width: int = screen_width
        self.__screen_height: int = screen_height
        self.__voice: Voice = Voice(voice_mode)
        self.__controller: object = controller
        pyautogui.FAILSAFE = False

    def _start_action(self) -> None:
        """
        action when program launched
        :return:
        """
        print('run')
        self.__voice._launch()
        time.sleep(0.3)
        self.__voice._play_voice_line('start')

    def _wait_to_speak(self, waiting: int) -> bool:
        """
        used to make the mouse unspeakable for giving time
        :param waiting:
        :return:
        """
        waiting -= 1
        time.sleep(0.3)
        if waiting <= 0:
            return True
        else:
            return False

    """
    =======================================
    movement method
    =======================================
    """

    def _first_move_action(self, started, axes_difference) -> bool:
        """
        use for the first move when program is launched
        :param started:
        :param axes_difference:
        :return:
        """
        if not started and axes_difference > 60:
            self.__voice._play_voice_line('firstMove')
            return True

    def _confused_action_movement(self) -> None:
        """
        action when state confused
        :return:
        """
        self.__voice._play_voice_line('confused', True)

    def _fast_move_x(self, x_position: int = 960, y_position: int = 540) -> None:
        """
        make to the __mouse fast and random direction
        :return:
        """
        self.__voice._play_voice_line('fast')
        confused = True if randint(1, 100) <= 25 else False
        while mixer.music.get_busy():
            pyautogui.moveTo(x=randint(0, self.__screen_width), y=randint(0, self.__screen_height),
                             duration=self.__speed)
        if confused:
            self.__controller.position = (x_position, y_position)
            self._confused_action_movement()

    def _slow_move_x(self) -> bool:
        """
        action on slow move for x axes
        :return:
        """
        speak = True if randint(1, 100) <= 10 else False
        if speak:
            self.__voice._play_voice_line('slow_move')
            return True
        else:
            return False

    def _medium_move_x(self):
        """
        action for medium move on x axes
        :return:
        """
        speak = True if randint(1, 100) <= 10 else False
        if speak <= 10:
            self.__voice._play_voice_line('medium')
            return True
        else:
            return False

    def _go_up_movement(self):
        """
        used when mouse y axes go up
        :return:
        """
        self.__voice._play_voice_line('up')

    def _hit_screen_border_x_movement(self):
        """
        action to do when the mouse hit the border of the screen
        :return:
        """
        self.__voice._play_voice_line('border')

    """
    =======================================
    click method
    =======================================
    """

    def _click(self):
        speak = True if randint(1, 100) <= 25 else False
        if speak:
            self.__voice._play_voice_line('click')

    """
    =======================================
    scroll method
    =======================================
    """
    def _scrolled(self):
        speak = True if randint(1, 100) <= 10 else False
        if speak:
            self.__voice._play_voice_line('scroll')
