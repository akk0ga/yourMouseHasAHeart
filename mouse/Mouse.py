import time

from pynput.mouse import Button, Controller


class Mouse:
    def __init__(self, x=0, y=0):
        """
        x is the X mouse's axe and y is the Y mouse's axe
        :param x:
        :param y:
        """
        self.__controller = Controller()
        self.__x = x
        self.__y = y

    def get_axes(self, pause=0):
        """
        get the mouse axes, pause is used to make a pause int the axes printing
        :param pause:
        :rtype: string
        """
        x, y = self.__controller.position
        print('=======================================')
        print(f'X: {x}\nY: {y}')
        print(time.thread_time())
        print('=======================================\n')
        time.sleep(pause)

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
