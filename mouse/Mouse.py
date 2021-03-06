import time
from pynput import mouse
from pygame import mixer

from mouse.Listener import Listener
from mouse.Action import Action


class Mouse(Listener, Action):

    def __init__(self, silence_time: int = 15, screen_width: int = 1920, screen_height: int = 1080,
                 voice_mode: str = 'en'):
        """
        create mouse instance, silence_time is default 15 for 5 sec if you want 10 sec set
        to 30
        :param silence_time:
        :param screen_width:
        :param screen_height:
        :param voice_mode:
        """
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

    """
    =======================================
    general method
    =======================================
    """

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
        self.__controller.position = (self.__x / 2, self.__y / 2)

    def start(self) -> None:
        """
        when the program is launched
        :return:
        """
        self._set_position()
        self.__action._start_action()

    """
    =======================================
    movement method
    =======================================
    """

    def __axes_difference(self, original_axes: tuple, new_axes: tuple) -> tuple:
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
        result: tuple = (abs(original_x - new_x), (new_y - original_y))
        return result

    def __x_axes_movement(self, x_axes_difference: int) -> None:
        """
        check the x axes of the mouse to choose the right acion to do
        :param axes_difference:
        :return:
        """
        if x_axes_difference > 1000:
            width = int(self.__x / 2)
            height = int(self.__y / 2)
            self.__action._fast_move_x(width, height)

        elif 300 < x_axes_difference < 500:
            if self.__action._slow_move_x():
                self.__can_speak = False

        elif 500 < x_axes_difference < 1000:
            if self.__action._action_medium_move_x():
                self.__can_speak = False

    def __y_axes_movement(self, y_axes_difference) -> None:
        """
        test the y axes difference to launch or not action
        :param y_axes_difference:
        :return:
        """
        if y_axes_difference > 400:
            self.__action._go_up_movement()
            self.__can_speak = False

    def __touch_border_screen(self, axes_difference: int) -> None:
        """
        check if the mouse touch the border of the screen
        :param axes_difference:
        :return:
        """
        x, y = self.get_axes()

        if axes_difference > 200 and (x == 0 or x == self.__x - 1):
            self.__action._hit_screen_border_x_movement()

    def __first_move(self, axes_difference: int) -> None:
        """
        for the first mouse movement when the program start
        :param axes_difference:
        :return:
        """
        launched = self.__action._first_move_action(self.__started, axes_difference)
        self.__started = launched

    def listener_mouse_movement(self, original_axes):
        time.sleep(0.3)
        new_axes: tuple = self.get_axes()
        difference: tuple = self.__axes_difference(new_axes, original_axes)
        x_difference, y_difference = difference

        self.__touch_border_screen(x_difference)

        # check if mouse can speak
        if self.__can_speak:
            # check if first time program run
            if not self.__started:
                self.__first_move(x_difference)

            # movement action
            self.__x_axes_movement(x_difference)
            self.__y_axes_movement(y_difference)

        # if speak is false
        else:
            # check if the silence time is done
            if self.__action._wait_to_speak(self.__silence_time):
                self.__silence_time = 15
                self.__can_speak = True
                print('end wait')
            else:
                self.__silence_time -= 1

    """
    =======================================
    click method
    =======================================
    """

    def __click(self) -> None:
        self.__action._action_click()

    def listener_mouse_click(self):
        self.__click()

    """
    =======================================
    listener method
    =======================================
    """

    def listener_mouse(self) -> None:
        """
        listen what you are doing on the mouse
        :return:
        """
        # listen __mouse event
        with mouse.Events() as events:
            for event in events:
                if hasattr(event, 'button'):
                    print('\n\nCLICKED\n\n')
                    self.listener_mouse_click()
                else:
                    original = self.get_axes()
                    self.listener_mouse_movement(original)
                    if self.__can_speak:
                        break

    """
    =======================================
    getter & setter
    =======================================
    """

    def set_x(self, x: int) -> None:
        self.__x = x

    def set_y(self, y: int) -> None:
        self.__y = y

    x = property(fset=set_x)
    y = property(fset=set_y)
