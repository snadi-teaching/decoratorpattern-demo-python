from .notifier_decorator import NotifierDecorator


class SMSDecorator(NotifierDecorator):
    def send_notification(self, message: str) -> None:
        super().send_notification(message)
        self.send_sms(message)

    def send_sms(self, message: str) -> None:
        print(f"Sent {message} via SMS")
