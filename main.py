# maybe i used those import winsound, pyautogui, pynput
from mouse.Mouse import Mouse


class Main:

    def __init__(self):
        self.mouse = Mouse()

    def run(self):
        while True:
            self.mouse.get_axes()


if __name__ == '__main__':
    program = Main()
    program.run()
