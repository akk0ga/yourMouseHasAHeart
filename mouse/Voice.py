from pygame import mixer
from random import randint
import os.path
import time

class Voice:
    def __init__(self, voice_mode):
        """
        this class is used to choose the correct voice line on the action
        """
        self.__volume: float = 0.2
        self.__voice_mode: str = voice_mode
        mixer.init()

    """
    =======================================
    general method
    =======================================
    """
    def __play(self, type: str) -> None:
        """
        play the music and set the volume
        :return:
        """
        mixer.music.load(self.__choose_file(type))
        mixer.music.play()
        mixer.music.set_volume(self.__volume)

    def __choose_file(self, type: str) -> str:
        """
        choose file to load
        :param type:
        :return:
        """
        num_files = len([f for f in os.listdir(f'voice/{type}/{self.__voice_mode}')])
        index = randint(1, num_files)
        return f'voice/{type}/{self.__voice_mode}/{type}_{self.__voice_mode}_{index}.wav'

    """
    =======================================
    launch method
    =======================================
    """
    def _launch(self) -> None:
        """
        voice played when program turn on
        :return:
        """
        mixer.music.load(f'voice/start/start.wav')
        mixer.music.play()
        mixer.music.set_volume(self.__volume)

    """
    =======================================
    choose the voice to play method
    =======================================
    """
    def _play_voice_line(self, type: str, confused: bool = False) -> None:
        """
        this method play voice line for the choosen type
        if confused set the param on True
        if program is launch set launch on True
        :param type:
        :return:
        """
        if not confused:
            self.__play(type)
        else:
            time.sleep(0.3)
            self._launch()
            time.sleep(0.3)
            self.__play(type)

    """
    =======================================
    getter & setter
    =======================================
    """
    def set_volume(self, volume: float) -> None:
        self.__volume = volume

    def get_volume(self) -> float:
        return self.__volume

    volume = property(get_volume, set_volume)
