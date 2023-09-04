from datetime import timedelta
from time import time

from utils.logging import debug

from .notifications import SlackNotifications
        
class PendingDepositsNotification():
    notifier: SlackNotifications
    pool_name: str
    explorer_url_prefix: str

    def __init__(self, _notifier: SlackNotifications, _pool: str, _explorer_url_prefix: str):
        self.notifier = _notifier
        self.pool_name = _pool
        self.explorer_url_prefix = _explorer_url_prefix

    def report_for_txs(self, _txs: list):
        slack_message = self.get_slack_message(_txs)
        self.notifier.send_notification(slack_message)

    def get_slack_message(self, _txs: list) -> dict:
        def format_timedelta(delta_seconds: int) -> str:
            delta = timedelta(seconds=delta_seconds)
            days = delta.days
            hours, remainder = divmod(delta.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            if days > 0:
                return f"{days} {'days' if days > 1 else 'day'} {hours} {'hrs' if hours > 1 else 'hr'} {minutes} {'mins' if minutes > 1 else 'min'}"
            else:
                return f"{hours} {'hrs' if hours > 1 else 'hr'} {minutes} {'mins' if minutes > 1 else 'min'}"

        debug(f'Composing the message')

        message = {
            "blocks": [
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "Direct deposit(s) stuck"
                    }
                },
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": f"*Pool:* {self.pool_name}"
                        }
                    ]
                },
                {
                    "type": "section",
                    "fields": [
                        {
                            "type": "mrkdwn",
                            "text": f"{len(_txs)} transaction(s) stuck:"
                        }
                    ]
                }
            ]
        }

        now = int(time())
        for tx in _txs:
            short_tx = f"{tx['hash'][:10]}...{tx['hash'][-8:]}"
            td = format_timedelta(now - tx['ts'])
            button_id = short_tx
            message['blocks'].append(
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": f'`{short_tx}` more than {td}'
                    },
                    "accessory": {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "View",
                            "emoji": False
                        },
                        "value": button_id,
                        "url": f"{self.explorer_url_prefix}{tx['hash']}",
                        "action_id": "button-action"
                    }
                }
            )

        return message