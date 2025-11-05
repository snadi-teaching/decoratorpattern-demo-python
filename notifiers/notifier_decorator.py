from .notifier import Notifier


class NotifierDecorator(Notifier):
    def __init__(self, wrappee: Notifier) -> None:
        self._wrappee = wrappee

    def send_notification(self, message: str) -> None:
        self._wrappee.send_notification(message)
