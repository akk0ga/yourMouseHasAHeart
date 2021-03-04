import time
from pynput import mouse
from pygame import mixer

from mouse.Listener import Listener
from mouse.Action import Action


class Mouse(Listener, Action):

    def __init__(self, silence_time: int = 5, screen_width: int = 1920, screen_height: int = 1080, voice_mode: str = 'en'):
        self.__controller = mouse.Controller()
        super().__init__(controller=self.__controller)

        # set the mixer param for playing sound
        mixer.init()
        mixer.music.set_volume(0.5)

        # attribute
        self.__x: int = screen_width
        self.__y: int = screen_height
        self.__action: Action = Action(controller=self.__controller, screen_width=screen_width,
                                       screen_height=screen_height, voice_mode=voice_mode)
        self.__started: bool = False
        self.__can_speak = True
        self.__silence_time = silence_time

        # for the log
        self.log: str = 'log/log.txt'

    def get_axes(self) -> tuple:
        """
        get the __mouse axes
        :rtype: tuple
        """
        original_axes: tuple = self.__controller.position
        return original_axes

    def _set_position(self) -> None:
        """
        set mouse position
        :rtype: None
        """
        self.__controller.position = (self.__x/2, self.__y/2)

    def on_move(self, x, y) -> None:
        """debug the mouse position on the screen"""
        self.__x: int = x
        self.__y: int = y
        print('=======================================')
        print(f'new position\n\tX: {x}\n\tY: {y}')
        print('=======================================\n')

    def __axes_difference(self, original_axes: tuple, new_axes: tuple) -> int:
        """
        get the difference for each mouse movement
        :param original_axes:
        :param new_axes:
        :return:
        """
        # split tuple
        original_x, original_y = original_axes
        new_x, new_y = new_axes

        # make the difference between axes x atm
        result: int = original_x - new_x
        return abs(result)

    def __x_axes_movement(self, axes_difference: int) -> None:
        """
        check the x axes of the mouse to choose the right acion to do
        :param axes_difference:
        :return:
        """
        if axes_difference > 1000:
            width = int(self.__x/2)
            height = int(self.__y/2)
            self.__action._fast_move_x(width, height)
            self.__can_speak = False

        elif 0 < axes_difference < 200:
            if self.__action._slow_move_x():
                self.__can_speak = False

        elif 400 < axes_difference < 900:
            if self.__action._action_medium_move_x():
                self.__can_speak = False

    def __touch_border_screen(self, axes_difference: int) -> None:
        """
        check if the mouse touch the border of the screen
        :param axes_difference:
        :return:
        """
        x, y = self.get_axes()

        if axes_difference > 200 and (x == 0 or x == self.__x-1):
            self.__action._hit_screen_border_x()

    def __first_move(self, axes_difference: int) -> None:
        """
        for the first mouse movement when the program start
        :param axes_difference:
        :return:
        """
        launched = self.__action._first_move_action(self.__started, axes_difference)
        self.__started = launched

    def start(self) -> None:
        """
        when the program is launched
        :return:
        """
        self._set_position()
        self.__action._start_action()

    def listener_event_mouse(self) -> None:
        # listen __mouse event
        with mouse.Events() as event:
            original_axes: tuple = self.get_axes()
            time.sleep(0.3)

        # if __mouse move
        if event:
            if not mixer.music.get_busy():
                new_axes: tuple = self.get_axes()
                difference: int = self.__axes_difference(new_axes, original_axes)

                self.__touch_border_screen(difference)

                # check if mouse can speak
                if self.__can_speak:
                    # check if first time program run
                    if not self.__started:
                        self.__first_move(difference)
                    self.__x_axes_movement(difference)
                # if speak is false
                else:
                    # check if the silence time is done
                    if self.__action._wait_to_speak(self.__silence_time):
                        self.__silence_time = 5
                        self.__can_speak = True
                        print('end wait')
                    else:
                        self.__silence_time -= 1

                print(difference)

            """
            with open(self.log, 'a') as log:
                log.write(f'{self.__axes_difference(new_axes, original_axes)}\n')
                log.close()
            """

    """
    attribute parameter
    """

    def set_x(self, x: int) -> None:
        self.__x = x

    def set_y(self, y: int) -> None:
        self.__y = y

    def get_x(self) -> int:
        return self.__x

    def get_y(self) -> int:
        return self.__y

    x = property(get_x, set_x)
    y = property(get_y, set_y)
