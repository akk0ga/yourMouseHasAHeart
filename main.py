# maybe i used those import winsound, pyautogui, pynput
from mouse.Mouse import Mouse


class Main:

    def __init__(self):
        self.mouse = Mouse(4)

    def run(self):
        print(self.mouse.x)
        self.mouse.x = 2
        print(self.mouse.x)


if __name__ == '__main__':
    program = Main()
    program.run()
