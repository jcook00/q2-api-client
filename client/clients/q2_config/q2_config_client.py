from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.q2_config_endpoints import Q2ConfigEndpoint


class Q2ConfigClient(BaseQ2Client):

    def get_q2_config(self):
        endpoint = Q2ConfigEndpoint.Q2_CONFIG.value
        return self._get(url=self._build_url(endpoint))
