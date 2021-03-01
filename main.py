import winsound, pyautogui, pynput
from pynput.mouse import Listener


def on_move(x, y):
    print('on move')


if __name__ == '__main__':
    with Listener(on_move=on_move) as listener:
        listener.join()
