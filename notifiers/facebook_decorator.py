from .notifier_decorator import NotifierDecorator


class FacebookDecorator(NotifierDecorator):
    def send_notification(self, message: str) -> None:
        super().send_notification(message)
        self.send_facebook(message)

    def send_facebook(self, message: str) -> None:
        print(f"Sent {message} to Facebook")
