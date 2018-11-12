from client.clients.q2_client import Q2Client
from client.endpoints.refresh_cache import RefreshCacheEndpoint


class RefreshCacheClient(Q2Client):

    def refresh_cache(self):
        endpoint = RefreshCacheEndpoint.REFRESH_CACHE.value
        return self._post(url=self._build_url(endpoint))
