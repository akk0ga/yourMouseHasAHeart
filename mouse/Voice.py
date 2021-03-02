from pygame import mixer
from random import randint


class Voice:
    def __init__(self):
        """
        this class is used to choose the correct voice line on the action
        """
        self.__volume = 0.2
        mixer.init()

    def __play(self):
        """
        play the music and set the volume
        :return:
        """
        mixer.music.play()
        mixer.music.set_volume(self.__volume)

    def start(self):
        """
        voice launch only one time when program is launched
        :return:
        """
        quote = randint(0, 3)
        mixer.music.load(f'voice/start/hello_{quote}.wav')
        self.__play()

    def move_fast_x(self):
        """
        this is used when the __mouse move fast
        :return void:
        """
        quote = randint(0, 2)
        mixer.music.load('voice/fast/fast_.wav')
        self.__play()

    def move_slow_x(self):
        """
        this is used when the __mouse go slow and randomize or not a sound
        :return void:
        """
        mixer.music.load('voice/baka_1.wav')
        self.__play()

    def set_volume(self, volume):
        self.__volume = volume

    def get_volume(self):
        return self.__volume

    def del_volume(self):
        del self.__volume

    volume = property(get_volume, set_volume, del_volume)
