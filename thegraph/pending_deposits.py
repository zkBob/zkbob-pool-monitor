from typing import List

from time import time

from sgqlc.operation import Operation

from graphql_schemas.zkbob_pool_schema import zkbob_pool_schema

from utils.logging import info, debug

from .base import TheGraphRequest

class PendingDirectDeposits():
    executor: TheGraphRequest
    submit_threshold: int = 60 * 60

    def __init__(self, _executor: TheGraphRequest, _threshold: int):
        self.executor = _executor
        self.submit_threshold = _threshold

    def request(self) -> List:
        query_def = Operation(zkbob_pool_schema.Query)

        dd_pending = query_def.direct_deposits(
            order_by = zkbob_pool_schema.DirectDeposit_orderBy.index,
            where = {"pending":True, "ts_init_lte": int(time()) - self.submit_threshold}
        )
        dd_pending.index()
        dd_pending.tx_init()
        dd_pending.ts_init()

        response_json = self.executor.get(query_def)

        if response_json == None:
            return []
        
        retval = (query_def + response_json).direct_deposits
        if len(retval) > 0:
            info(f'Discovered {len(retval)} pending direct deposits')    
        else:
            debug(f'Discovered {len(retval)} pending direct deposits')

        return retval

        


