from .notifier_decorator import NotifierDecorator


class SlackDecorator(NotifierDecorator):
    def send_notification(self, message: str) -> None:
        super().send_notification(message)
        self.send_to_slack(message)

    def send_to_slack(self, message: str) -> None:
        print(f"Sent {message} to SLACK")
