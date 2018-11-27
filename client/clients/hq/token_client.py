from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.hq_endpoints import TokenEndpoint


class TokenClient(BaseQ2Client):

    def get_token_info(self):
        """GET /hq/tokeninfo

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = TokenEndpoint.TOKEN_INFO.value
        return self._get(url=self._build_url(endpoint))
