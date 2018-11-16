from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import NavEndpoint


class NavClient(BaseQ2Client):

    def get_navigation_menu(self):
        endpoint = NavEndpoint.NAV.value
        return self._get(url=self._build_url(endpoint))
