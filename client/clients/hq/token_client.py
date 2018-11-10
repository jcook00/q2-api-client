from client.clients.q2_client import Q2Client
from client.endpoints.hq import TokenEndpoint


class TokenClient(Q2Client):

    def get_token_info(self):
        endpoint = TokenEndpoint.TOKEN_INFO.value
        return self.get(url=self.build_url(endpoint))
