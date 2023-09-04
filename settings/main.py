from functools import cache
from pydantic import BaseSettings

from json import load

from utils.logging import info, error

from .models import PoolConfig, ListOfPools

class GenericSettings(BaseSettings):
    _extra_sources = []
    _formatters = {}

    def extend_extra_sources(self, source):
        self._extra_sources.append(source)

    def extend_formatters(self, formatter: dict):
        self._formatters.update(formatter)
        
    @classmethod
    @cache
    def get(cls):
        settings = cls()

        # init of fields that cannot be filled by Config::customise_sources approach
        for fn in cls._extra_sources:
            fn()

        for (key, value) in settings:
            to_out = value
            if key in cls._formatters:
                to_out = cls._formatters[key](value)
            info(f'{key.upper()} = {to_out}')

        return settings

    class Config:
        env_file = ".env"

class Settings(GenericSettings):
    monitoring_interval: int = 60 * 60
    pools_config_file: str = 'pools-config.json'
    pools: ListOfPools = []
    simulate_sending: bool = False
    loglevel: str = 'INFO'

    def __init__(self):
        def read_pools_config():
            # this source cannot be used through Config::customise_sources approach
            # since token_depoloyments_info can be default at the moment of the source applying
            fname = self.pools_config_file
            info(f'Load pools configs from {fname}')

            try:
                with open(fname) as f:
                    read_pools = load(f)['pools']
            except IOError as e:
                error(f'Cannot read pools configs')
                raise e

            for p in read_pools:
                self.pools.append(PoolConfig.parse_obj(p))

        def pools_formatter(_pools: ListOfPools) -> str:
            retval = []
            for p in _pools:
                retval.append(p.name)

            return str(retval)

        super().__init__()

        self.extend_extra_sources(read_pools_config)
        self.extend_formatters({'pools': pools_formatter})

    

