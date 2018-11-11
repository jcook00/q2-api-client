from client.clients.v2.banking_client import BankingClient
from client.clients.v2.commercial_client import CommercialClient
from client.clients.v2.pfm_client import PFMClient


class V2Client:

    def __init__(self, **kwargs):
        self._banking = BankingClient(**kwargs)
        kwargs['q2token'] = self._banking.get_header('q2token')
        self._commercial = CommercialClient(**kwargs)
        self._pfm = PFMClient(**kwargs)

    @property
    def banking(self):
        return self._banking

    @property
    def commercial(self):
        return self._commercial

    @property
    def pfm(self):
        return self._pfm
