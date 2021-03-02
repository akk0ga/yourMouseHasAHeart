import time

from pynput import mouse
from mouse.Listener import Listener
from pygame import mixer


class Mouse(Listener):

    def __init__(self, x=0, y=0):
        """
        x is the X mouse's axe and y is the Y mouse's axe, this class is used
        to get the mouse event
        :param x:
        :param y:
        """
        #set the mixer param for playing sound
        mixer.init()
        mixer.music.set_volume(0.5)

        #attribute
        self.__controller = mouse.Controller()
        self.__x = x
        self.__y = y
        self.__sound = {
            'fast': 'music/fast.wav',
            'short': 'music/baka_1.wav'
        }
        self.test = 0
        mixer.music.load(self.__sound['short'])

    def get_axes(self):
        """
        get the mouse axes
        :rtype: string
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

    def listener_mouse_move(self):
        with mouse.Listener(on_move=self.__on_move) as listener:
            listener.join()

    def listener_event_mouse(self):
        with mouse.Events() as event:
            original_x, original_y = self.get_axes()
            time.sleep(0.2)
        if event:
            new_x, new_y = self.get_axes()
            print('=======================================')
            print(f'new position\n\tX: {new_x}\n\tY: {new_y}')
            print('=======================================\n')

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
