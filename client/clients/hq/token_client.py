from client.clients.q2_client import Q2Client
from client.endpoints.hq import TokenEndpoint


class TokenClient(Q2Client):

    def get_token_info(self):
        endpoint = TokenEndpoint.TOKEN_INFO.value
        return self._get(url=self._build_url(endpoint))
