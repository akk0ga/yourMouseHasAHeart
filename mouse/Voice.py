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

    def __play(self, type: str):
        """
        play the music and set the volume
        :return:
        """
        mixer.music.load(self.__choose_file(type))
        mixer.music.play()
        mixer.music.set_volume(self.__volume)

    def __choose_file(self, type: str):
        num_files = len([f for f in os.listdir(f'voice/{type}/{self.__voice_mode}')])
        index = randint(1, num_files)
        return f'voice/{type}/{self.__voice_mode}/{type}_{self.__voice_mode}_{index}.wav'

    def _launch(self):
        mixer.Sound(f'voice/start/start.wav').set_volume(self.__volume)
        mixer.Sound(f'voice/start/start.wav').play()

    def _start(self):
        """
        voice launch only one time when program is launched
        :return:
        """
        self.__play('start')

    def _move_fast_x(self):
        """
        this is used when the __mouse move fast
        :return void:
        """
        self.__play("fast")

    def _confused(self):
        """
        play voice when state is confused
        :return:
        """
        time.sleep(0.3)
        self._launch()
        time.sleep(0.3)
        self.__play('confused')

    def set_volume(self, volume):
        self.__volume = volume

    def get_volume(self):
        return self.__volume

    volume = property(get_volume, set_volume)
