from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import ThemeEndpoint


class ThemeClient(BaseQ2Client):

    def get_theme(self):
        endpoint = ThemeEndpoint.THEME.value
        return self._get(url=self._build_url(endpoint))

    def update_theme(self, **request_body):
        endpoint = ThemeEndpoint.THEME.value
        return self._put(url=self._build_url(endpoint), json=request_body)
