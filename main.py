# maybe i used those import winsound, pyautogui, pynput
from mouse.Mouse import Mouse
from pynput import mouse
from pygame import mixer


class Main:

    def __init__(self):
        self.mouse = Mouse()
        self.mouse.x = 0
        self.mouse.y = 0

    def run(self):
        # self.mouse.listener_mouse_move()
        self.mouse.listener_event_mouse()

if __name__ == '__main__':
    program = Main()
    program.run()
