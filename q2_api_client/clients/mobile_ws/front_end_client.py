from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import FrontEndEndpoint


class FrontEndClient(BaseQ2Client):

    def get_front_end_config(self):
        """GET /mobilews/frontEndConfig

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FrontEndEndpoint.FRONT_END_CONFIG.value
        return self._get(url=self._build_url(endpoint))

    def create_front_end_config(self, request_body):
        """POST /mobilews/frontEndConfig

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FrontEndEndpoint.FRONT_END_CONFIG.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_front_end_config(self, request_body):
        """PUT /mobilews/frontEndConfig

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = FrontEndEndpoint.FRONT_END_CONFIG.value
        return self._put(url=self._build_url(endpoint), json=request_body)
