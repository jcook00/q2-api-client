from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.q2_config_endpoints import Q2ConfigEndpoint


class Q2ConfigClient(BaseQ2Client):

    def get_q2_config(self):
        """GET /q2config

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = Q2ConfigEndpoint.Q2_CONFIG.value
        return self._get(url=self._build_url(endpoint))
