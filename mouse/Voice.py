from pygame import mixer
from random import randint

class Voice:
    def __init__(self):
        """
        this class is used to choose the correct voice line on the action
        """
        self.__volume = 0.5
        self.__file ={
            'short': mixer.music.load('music/baka_1.wav'),
            'fast': mixer.music.load('music/fast.wav')
        }
        mixer.init()

    def move_fast_x(self, difference_calc, difference_request):
        """
        this is used when the mouse move fast
        :param difference_calc:
        :param difference_request:
        :return void:
        """
        while difference_calc > difference_request:
            if not mixer.music.get_busy():
                mixer.music.load('music/short.wav')
                mixer.music.play()
                mixer.music.set_volume(0.2)


    def move_slow_x(self, difference_calc, difference_request):
        """
        this is used when the mouse go slow and randomize or not a sound
        :param difference_calc:
        :param difference_request:
        :return void:
        """
        if difference_calc > difference_request and not mixer.get_busy():
            self.__file['short'].play()

    def set_volume(self, volume):
        self.__volume = volume

    def get_volume(self):
        return self.__volume

    def del_volume(self):
        del self.__volume

    volume = property(get_volume, set_volume, del_volume)
