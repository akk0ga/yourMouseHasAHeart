# maybe i used those import pyautogui
from mouse.Mouse import Mouse
from mouse.Voice import Voice

class Main:

    def __init__(self):
        self.mouse = Mouse()
        self.mouse.x = 510
        self.mouse.y = 0
        self.voice = Voice()

    def run(self):
        # self.mouse.listener_mouse_move()
        print('=======================================')
        print(f'original mouse position\n\tX: {self.mouse.get_axes()[0]}\n\tY: {self.mouse.get_axes()[1]}')
        print('=======================================\n')
        self.mouse.set_position()
        while True:
            self.mouse.listener_event_mouse()


if __name__ == '__main__':
    program = Main()
    program.run()
