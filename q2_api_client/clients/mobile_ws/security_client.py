from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import SecurityEndpoint


class SecurityClient(BaseQ2Client):

    def change_password(self, request_body):
        """POST /mobilews/changePassword

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SecurityEndpoint.CHANGE_PASSWORD.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def validate_password(self, request_body):
        """POST /mobilews/validatePassword

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = SecurityEndpoint.VALIDATE_PASSWORD.value
        return self._post(url=self._build_url(endpoint), json=request_body)
