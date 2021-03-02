import time

from pynput import mouse
from pygame import mixer

from mouse.Listener import Listener
from mouse.Voice import Voice
from mouse.Action import Action


class Mouse(Listener, Action):

    def __init__(self, x=0, y=0):
        super().__init__()
        """
        x is the X mouse's axe and y is the Y mouse's axe, this class is used
        to get the mouse event
        :param x:
        :param y:
        """
        # set the mixer param for playing sound
        mixer.init()
        mixer.music.set_volume(0.5)

        # attribute
        self.__controller = mouse.Controller()
        self.__x = x
        self.__y = y
        self.__voice = Voice()
        self.__action = Action()

        # for the log
        self.log = 'log/log.txt'

    def get_axes(self):
        """
        get the mouse axes
        :rtype: tuple
        """
        original_axes = self.__controller.position
        return original_axes

    def set_position(self):
        """
        set the mouse position to another axes
        :rtype: void
        """
        self.__controller.position = (self.__x, self.__y)

    def __on_move(self, x, y):
        """for mouse movement"""
        self.__x = x
        self.__y = y
        print('=======================================')
        print(f'new position\n\tX: {x}\n\tY: {y}')
        print('=======================================\n')

    def __axes_difference(self, original_axes: tuple, new_axes: tuple):
        # split tuple
        original_x, original_y = original_axes
        new_x, new_y = new_axes

        # make the difference between axes x atm
        result = original_x - new_x
        return abs(result)

    def listener_event_mouse(self):
        # listen mouse event
        with mouse.Events() as event:
            original_axes = self.get_axes()
            time.sleep(0.3)

        # if mouse move
        if event and not mixer.music.get_busy():
            new_axes = self.get_axes()
            difference = self.__axes_difference(new_axes, original_axes)

            # check choice
            if difference > 1000:
                self.__voice.move_fast_x()
                self.__action._fast_movement_random(1920, 1080)

            elif difference > 300:
                self.__voice.move_slow_x()
            print(self.__axes_difference(new_axes, original_axes))

            with open(self.log, 'a') as log:
                log.write(f'{self.__axes_difference(new_axes, original_axes)}\n')
                log.close()

    """
    attribute parameter
    """

    def set_x(self, x: int):
        self.__x = x

    def set_y(self, y: int):
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def del_x(self):
        del self.__x

    def del_y(self):
        del self.__y

    x = property(get_x, set_x, del_x)
    y = property(get_y, set_y, del_y)
