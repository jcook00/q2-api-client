from client.clients.central.central_client import CentralClient
from client.clients.file_map.file_map_client import FileMapClient
from client.clients.hq.hq_client import HQClient
from client.clients.q2_config.q2_config_client import Q2ConfigClient


class Q2APIClient:

    def __init__(self, **kwargs):
        self._q2_config = Q2ConfigClient(**kwargs)
        kwargs['q2token'] = self._q2_config.headers.get('q2token')
        self._central = CentralClient(**kwargs)
        self._file_map = FileMapClient(**kwargs)
        self._hq = HQClient(**kwargs)

    @property
    def q2_config(self):
        return self._q2_config

    @property
    def central(self):
        return self._central

    @property
    def file_map(self):
        return self._file_map

    @property
    def hq(self):
        return self._hq
