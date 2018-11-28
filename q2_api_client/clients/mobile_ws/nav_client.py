from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import NavEndpoint


class NavClient(BaseQ2Client):

    def get_navigation_menu(self):
        """GET /mobilews/nav

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = NavEndpoint.NAV.value
        return self._get(url=self._build_url(endpoint))
