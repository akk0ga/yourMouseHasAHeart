import time

from pynput import mouse
from pygame import mixer

from mouse.Listener import Listener
from mouse.Action import Action
from random import randint


class Mouse(Listener, Action):

    def __init__(self, screen_width: int = 960, screen_height: int = 540, voice_mode: str = 'en'):
        super().__init__()
        # set the mixer param for playing sound
        mixer.init()
        mixer.music.set_volume(0.5)

        # attribute
        self.__controller = mouse.Controller()
        self.__x: int = screen_width
        self.__y: int = screen_height
        self.__action: Action = Action(screen_width=screen_width, screen_height=screen_height, voice_mode=voice_mode)
        self.__started = False

        # for the log
        self.log: str = 'log/log.txt'

    def get_axes(self) -> tuple:
        """
        get the __mouse axes
        :rtype: tuple
        """
        original_axes: tuple = self.__controller.position
        return original_axes

    def _set_position(self) -> None:
        """
        set mouse position
        :rtype: None
        """
        self.__controller.position = (self.__x, self.__y)

    def on_move(self, x, y) -> None:
        """debug the mouse position on the screen"""
        self.__x: int = x
        self.__y: int = y
        print('=======================================')
        print(f'new position\n\tX: {x}\n\tY: {y}')
        print('=======================================\n')

    def __axes_difference(self, original_axes: tuple, new_axes: tuple) -> int:
        # split tuple
        original_x, original_y = original_axes
        new_x, new_y = new_axes

        # make the difference between axes x atm
        result: int = original_x - new_x
        return abs(result)

    def __x_axes_movement(self, axes_difference: int) -> None:
        if axes_difference > 1000:
            self.__action._fast_move_x(self.__controller, self.__x, self.__y)

    def __first_move(self, axes_difference: int):
        if not self.__started and axes_difference > 60:
            self.__action._first_move_action()
            self.__started = True

    def start(self) -> None:
        self._set_position()
        self.__action._start_action()

    def listener_event_mouse(self) -> None:
        # listen __mouse event
        with mouse.Events() as event:
            original_axes: tuple = self.get_axes()
            time.sleep(0.3)

        # if __mouse move
        if event and not mixer.music.get_busy():
            new_axes: tuple = self.get_axes()
            difference: int = self.__axes_difference(new_axes, original_axes)

            # check choice
            self.__first_move(difference)
            self.__x_axes_movement(difference)

            print(self.__axes_difference(new_axes, original_axes))

            """
            with open(self.log, 'a') as log:
                log.write(f'{self.__axes_difference(new_axes, original_axes)}\n')
                log.close()
            """

    """
    attribute parameter
    """

    def set_x(self, x: int) -> None:
        self.__x = x

    def set_y(self, y: int) -> None:
        self.__y = y

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    x = property(get_x, set_x)
    y = property(get_y, set_y)
