from typing import List, Union
from pydantic import BaseModel

class BaseMonitorConfig(BaseModel):
    mode: str

class PendingDDMonitorConfig(BaseMonitorConfig):
    deposit_submit_threshold: int = 60 * 60

class PoolConfig(BaseModel):
    name: str
    subgraph_endpoint: str
    slack_webhook: str
    explorer_prefix: str
    monitors: List[PendingDDMonitorConfig]

ListOfPools = List[PoolConfig]