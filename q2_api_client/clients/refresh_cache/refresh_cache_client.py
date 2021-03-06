from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.refresh_cache_endpoints import RefreshCacheEndpoint


class RefreshCacheClient(BaseQ2Client):

    def refresh_cache(self):
        """POST /refreshCache

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = RefreshCacheEndpoint.REFRESH_CACHE.value
        return self._post(url=self._build_url(endpoint))
