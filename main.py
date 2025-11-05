from notifiers.notifier import Notifier
from notifiers.sms_decorator import SMSDecorator
from notifiers.slack_decorator import SlackDecorator
from notifiers.facebook_decorator import FacebookDecorator


def get_user_input():
    return (
        input(
            "Select additional notification channels to enable (sms, facebook, slack). Choose done to stop:"
        )
        .strip()
        .lower()
    )


def get_notification_choices():
    selected_notifications = []

    choice = get_user_input()

    while choice != "done":
        if choice in ["sms", "facebook", "slack"]:
            selected_notifications.append(choice)
        else:
            print(f"Unknown option: {choice}")
        choice = get_user_input()

    return selected_notifications


def build_notifier(choices: list[str]) -> Notifier:
    notifier: Notifier = Notifier()

    for choice in choices:
        if choice == "sms":
            notifier = SMSDecorator(notifier)
        elif choice == "slack":
            notifier = SlackDecorator(notifier)
        elif choice == "facebook":
            notifier = FacebookDecorator(notifier)

    return notifier


def main():
    choices = get_notification_choices()
    notifier = build_notifier(choices)
    notifier.send_notification("Hello World!")


if __name__ == "__main__":
    main()
