from typing import List

from settings.main import Settings
from utils.scheduler import every

from monitors.base import BaseMonitor
from monitors.pending_dd import PendingDDMonitor

from thegraph.base import TheGraphRequest
from slack.notifications import SlackNotifications

from utils.logging import info, redefine_loglevel

class SubgraphsMonitor():
    active_monitors: List[BaseMonitor] = []
    
    known_monitors = {
        'PendingDD': PendingDDMonitor
    }

    def get_monitor_class(self, _mode: str) -> BaseMonitor:
        return self.known_monitors[_mode]

    def __init__(self, _settings: Settings):
        for pool in _settings.pools:

            executor = TheGraphRequest(pool.subgraph_endpoint)
            notifier = SlackNotifications(pool.slack_webhook, settings.simulate_sending)

            for monitor in pool.monitors:
                info(f'Active monitor: {monitor.mode} for {pool.name}')
                c = self.get_monitor_class(monitor.mode)
                self.active_monitors.append(c(pool, monitor, executor, notifier))

    def loop(self):
        for monitor in self.active_monitors:
            monitor.check_and_report()

if __name__ == '__main__':
    settings = Settings.get()
    redefine_loglevel(settings.loglevel)
    worker = SubgraphsMonitor(settings)
    every(
        worker.loop,
        settings.monitoring_interval
    )
