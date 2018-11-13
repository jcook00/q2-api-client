from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.refresh_cache_endpoints import RefreshCacheEndpoint


class RefreshCacheClient(BaseQ2Client):

    def refresh_cache(self):
        endpoint = RefreshCacheEndpoint.REFRESH_CACHE.value
        return self._post(url=self._build_url(endpoint))
