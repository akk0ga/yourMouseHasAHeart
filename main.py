from mouse.Mouse import Mouse
from win32api import GetSystemMetrics as screenSize
from pygame import mixer


class Main:

    def __init__(self):
        self.__screen_width: int = screenSize(0)
        self.__screen_height: int = screenSize(1)
        self.__mouse = Mouse(screen_width=self.__screen_width, screen_height=self.__screen_height, voice_mode='fr')
        mixer.init()

    def run(self):
        self.__mouse.start()
        while True:
            self.__mouse.listener_event_mouse()


if __name__ == '__main__':
    program = Main()
    program.run()