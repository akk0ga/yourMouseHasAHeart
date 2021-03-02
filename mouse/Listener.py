import abc


class Listener(abc.ABC):

    def listener_mouse_scroll(self):
        """listen the mouse scroll action"""
        pass

    def listener_mouse_click(self):
        """listen the mouse click action"""
        pass

    @abc.abstractmethod
    def listener_event_mouse(self):
        """used to listen event affect mouse"""
        pass