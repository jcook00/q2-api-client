from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import ThemeEndpoint


class ThemeClient(BaseQ2Client):

    def get_theme(self):
        """GET /mobilews/theme

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = ThemeEndpoint.THEME.value
        return self._get(url=self._build_url(endpoint))

    def update_theme(self, request_body):
        """PUT /mobilews/theme

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = ThemeEndpoint.THEME.value
        return self._put(url=self._build_url(endpoint), json=request_body)
