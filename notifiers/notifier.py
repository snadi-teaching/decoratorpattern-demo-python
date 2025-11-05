class Notifier:
    def send_notification(self, message: str) -> None:
        # assume that the base behavior is to always send email notifications
        print(f"Sending email notification with {message}!")
