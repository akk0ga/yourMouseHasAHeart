from pygame import mixer
from random import randint
import os.path
import time


class Voice:
    def __init__(self, voice_mode):
        """
        this class is used to choose the correct voice line on the action
        """
        self.__volume = 0.2
        self.__voice_mode = voice_mode
        mixer.init()

    def __play(self):
        """
        play the music and set the volume
        :return:
        """
        mixer.music.play()
        mixer.music.set_volume(self.__volume)

    def __choose_file(self, type: str):
        num_files = len([f for f in os.listdir(f'voice/{type}/{self.__voice_mode}')])
        return randint(1, num_files)

    def _launch(self):
        mixer.Sound(f'voice/start/start.wav').set_volume(self.__volume)
        mixer.Sound(f'voice/start/start.wav').play()

    def _start(self):
        """
        voice launch only one time when program is launched
        :return:
        """
        mixer.music.load(f'voice/start/{self.__voice_mode}/hello_{self.__voice_mode}_{self.__choose_file("start")}.wav')
        self.__play()

    def _move_fast_x_play(self):
        """
        this is used when the __mouse move fast
        :return void:
        """
        mixer.music.load(f'voice/fast/{self.__voice_mode}/fast_{self.__voice_mode}_{self.__choose_file("fast")}.wav')
        self.__play()

    def _confused(self):
        """
        play voice when state is confused
        :return:
        """
        time.sleep(0.3)
        self._launch()
        time.sleep(0.3)
        mixer.music.load(f'voice/confused/{self.__voice_mode}/confused_{self.__voice_mode}_{randint(1, 2)}.wav')
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
