from q2_api_client.clients.central.csr_client import CSRClient
from q2_api_client.clients.central.gam_client import GAMClient
from q2_api_client.clients.central.lookup_client import LookupClient


class CentralClient:

    def __init__(self, **kwargs):
        self._csr = CSRClient(**kwargs)
        kwargs['q2token'] = self._csr.get_header('q2token')
        self._gam = GAMClient(**kwargs)
        self._lookup = LookupClient(**kwargs)

    @property
    def csr(self):
        return self._csr

    @property
    def gam(self):
        return self._gam

    @property
    def lookup(self):
        return self._lookup
