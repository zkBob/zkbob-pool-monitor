from functools import cache

from requests import post

from utils.logging import info, error, debug

@cache
class SlackNotifications:
    incoming_webhook: str

    _simulate_sending: bool
    
    def __init__(self, _web_hook: str, _simulate: bool = False):
        debug(f'Slack messenger {_web_hook[-8:]}')
        self.incoming_webhook = _web_hook
        self._simulate_sending = _simulate
        
    def send_notification(self, _slack_message: dict):
        if not self._simulate_sending:
            info(f'Sending a message to Slack')
            try:
                post(
                    url = self.incoming_webhook,
                    json = _slack_message,
                    timeout = 2
                )
            except Exception as e:
                error(f'Cannot send the message: {e}')
        else:
            info(f'Simulate sending a message to Slack')

