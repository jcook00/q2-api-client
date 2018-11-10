from client.endpoints.q2_config import Q2ConfigEndpoint
from client.services.q2_service import Q2Client


class Q2ConfigService(Q2Client):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_q2_config(self):
        endpoint = Q2ConfigEndpoint.Q2_CONFIG.value
        return self.get(url=self.build_url(endpoint))
