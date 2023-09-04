from functools import cache

from sgqlc.operation import Operation
from sgqlc.endpoint.http import HTTPEndpoint

from utils.logging import error, info, debug

@cache
class TheGraphRequest():
    endpoint: str

    def __init__(self, _endpoint: str):
        debug(f'TheGraph query executor for {_endpoint}')
        self.endpoint = _endpoint

    def get(self, _query_definition: Operation): 
        headers = {}
        info(f'Requesting TheGraph by url {self.endpoint}')
        endpoint = HTTPEndpoint(self.endpoint, headers)

        retval = None
        try:
            retval = endpoint(_query_definition)
        except Exception as e:
            error(f'Cannot get TheGraph data: {e}')
        
        return retval