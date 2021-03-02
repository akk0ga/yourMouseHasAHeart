from pygame import mixer


class Voice:
    def __init__(self):
        """
        this class is used to choose the correct voice line on the action
        """
        self.__volume = 0.5
        self.__file ={
            'short': mixer.Sound('music/baka_1.wav'),
            'fast': mixer.Sound('music/fast.wav')
        }

        mixer.init()

    def __move_fast(self):
        """
        move fast is used when the mouse has a axes difference of min 500
        :return:
        """
        self.__file['short'].play()

    def set_volume(self, volume):
        self.__volume = volume

    def get_volume(self):
        return self.__volume

    def del_volume(self):
        del self.__volume

    volume = property(get_volume, set_volume, del_volume)
