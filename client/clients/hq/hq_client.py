from client.clients.hq.back_office_client import BackOfficeClient
from client.clients.hq.core_client import CoreClient
from client.clients.hq.front_end_client import FrontEndClient
from client.clients.hq.token_client import TokenClient


class HQClient:

    def __init__(self, **kwargs):
        self._back_office = BackOfficeClient(**kwargs)
        kwargs['q2token'] = self._back_office.get_header('q2token')
        self._core = CoreClient(**kwargs)
        self._front_end = FrontEndClient(**kwargs)
        self._token = TokenClient(**kwargs)

    @property
    def back_office(self):
        return self._back_office

    @property
    def core(self):
        return self._core

    @property
    def front_end(self):
        return self._front_end

    @property
    def token(self):
        return self._token
