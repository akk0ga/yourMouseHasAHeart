from pygame import mixer
from random import randint
import time


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

    def _launch(self):
        mixer.Sound(f'voice/start/start.wav').set_volume(self.__volume)
        mixer.Sound(f'voice/start/start.wav').play()

    def _start(self, voice_mode: str = 'en'):
        """
        voice launch only one time when program is launched
        :return:
        """
        mixer.music.load(f'voice/start/{voice_mode}/hello_{voice_mode}_{randint(1, 4)}.wav')
        self.__play()

    def _move_fast_x_choose(self):
        """
        on return the first index is the file and the second is the time of sound
        confused is for the turret try to find the user with quote
        :return: tuple
        """
        quote = randint(1, 2)
        confused = randint(0, 15)
        confused = True if confused < 16 else False
        if quote == 1:
            return 1, 1.5, confused
        if quote == 2:
            return 2, 2, confused

    def _move_fast_x_play(self, voice: int = 1):
        """
        this is used when the __mouse move fast
        :return void:
        """
        mixer.music.load(f'voice/fast/en/fast_en_{voice}.wav')
        self.__play()

    def _confused(self):
        """
        play voice when state is confused
        :return:
        """
        time.sleep(0.3)
        self._launch()
        time.sleep(0.3)
        mixer.music.load(f'voice/confused/en/confused_en_{randint(1, 2)}.wav')
        self.__play()

    def _move_slow_x(self):
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

    volume = property(get_volume, set_volume)
