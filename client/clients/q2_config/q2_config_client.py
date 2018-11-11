from client.clients.q2_client import Q2Client
from client.endpoints.q2_config import Q2ConfigEndpoint


class Q2ConfigClient(Q2Client):

    def get_q2_config(self):
        endpoint = Q2ConfigEndpoint.Q2_CONFIG.value
        return self._get(url=self._build_url(endpoint))
