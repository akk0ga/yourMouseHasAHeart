from pygame import mixer
from random import randint


class Voice:
    def __init__(self):
        """
        this class is used to choose the correct voice line on the action
        """
        self.__volume = 0.2
        mixer.init()

    def move_fast_x(self):
        """
        this is used when the mouse move fast
        :return void:
        """
        mixer.music.load('voice/fast.wav')
        mixer.music.play()
        mixer.music.set_volume(self.__volume)

    def move_slow_x(self):
        """
        this is used when the mouse go slow and randomize or not a sound
        :return void:
        """
        mixer.music.load('voice/baka_1.wav')
        mixer.music.play()
        mixer.music.set_volume(self.__volume)

    def set_volume(self, volume):
        self.__volume = volume

    def get_volume(self):
        return self.__volume

    def del_volume(self):
        del self.__volume

    volume = property(get_volume, set_volume, del_volume)
