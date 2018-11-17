from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import FrontEndEndpoint


class FrontEndClient(BaseQ2Client):

    def get_front_end_config(self):
        endpoint = FrontEndEndpoint.FRONT_END_CONFIG.value
        return self._get(url=self._build_url(endpoint))

    def create_front_end_config(self, **request_body):
        endpoint = FrontEndEndpoint.FRONT_END_CONFIG.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_front_end_config(self, **request_body):
        endpoint = FrontEndEndpoint.FRONT_END_CONFIG.value
        return self._put(url=self._build_url(endpoint), json=request_body)
