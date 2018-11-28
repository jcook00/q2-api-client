from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import ConfigEndpoint


class ConfigClient(BaseQ2Client):

    def get_uux_configuration(self):
        """GET /mobilews/uuxConfiguration

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = ConfigEndpoint.UUX_CONFIGURATION.value
        return self._get(url=self._build_url(endpoint))

    def delete_uux_configuration(self):
        """DELETE /mobilews/uuxConfiguration

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = ConfigEndpoint.UUX_CONFIGURATION.value
        return self._delete(url=self._build_url(endpoint))

    def create_uux_configuration(self, request_body):
        """POST /mobilews/uuxConfiguration

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = ConfigEndpoint.UUX_CONFIGURATION.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_uux_configuration(self, request_body):
        """PUT /mobilews/uuxConfiguration

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = ConfigEndpoint.UUX_CONFIGURATION.value
        return self._put(url=self._build_url(endpoint), json=request_body)
