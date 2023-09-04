from thegraph.base import TheGraphRequest
from thegraph.pending_deposits import PendingDirectDeposits

from slack.notifications import SlackNotifications
from slack.pending_deposits import PendingDepositsNotification

from settings.models import PoolConfig, PendingDDMonitorConfig
from utils.logging import info

from .base import BaseMonitor

class PendingDDMonitor(BaseMonitor):
    reader: PendingDirectDeposits
    reporter: PendingDepositsNotification

    def __init__(self, 
                 _pool_settings: PoolConfig, 
                 _monitor_settings: PendingDDMonitorConfig,
                 _executor: TheGraphRequest,
                 _notifier: SlackNotifications
                 ):
        self.reader = PendingDirectDeposits(_executor, _monitor_settings.deposit_submit_threshold)
        self.reporter = PendingDepositsNotification(_notifier, _pool_settings.name, _pool_settings.explorer_prefix)

    def check_and_report(self):
        info(f'Checking pending direct deposits on {self.reporter.pool_name}')
        txs = [ {'hash': d.tx_init, 'ts': int(d.ts_init)} for d in self.reader.request()]
        if len(txs) > 0:
            self.reporter.report_for_txs(txs)        
