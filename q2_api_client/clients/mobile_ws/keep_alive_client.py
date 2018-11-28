from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import KeepAliveEndpoint


class KeepAliveClient(BaseQ2Client):

    def keep_alive(self):
        """GET /mobilews/keepalive

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = KeepAliveEndpoint.KEEP_ALIVE.value
        return self._get(url=self._build_url(endpoint))
