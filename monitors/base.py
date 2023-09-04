from settings.models import PoolConfig, PendingDDMonitorConfig
from thegraph.base import TheGraphRequest
from slack.notifications import SlackNotifications

class BaseMonitor():
    def __init__(self, 
                 _pool_settings: PoolConfig, 
                 _monitor_settings: PendingDDMonitorConfig,
                 _executor: TheGraphRequest,
                 _notifier: SlackNotifications
                 ):
        pass

    def check_and_report(self):
        pass