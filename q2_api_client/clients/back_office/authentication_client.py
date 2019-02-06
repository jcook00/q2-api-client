from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.back_office_endpoints import AuthenticationEndpoint


class AuthenticationClient(BaseQ2Client):

    def login(self, request_body):
        """POST /backoffice/v3/login

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AuthenticationEndpoint.LOGIN.value
        return self._post(url=self._build_url(endpoint), json=request_body)
