import time


class Timer:
    def __init__(self, move_time=0.3):
        """this class have method wich were used for mouse event"""
        self.__move_time = float(move_time)

    def set_move_time(self, new_move_time):
        self.__move_time = new_move_time

    def get_move_time(self):
        return self.__move_time

    def del_move_time(self):
        del self.__move_time

    move_time = property(get_move_time, set_move_time, del_move_time)
