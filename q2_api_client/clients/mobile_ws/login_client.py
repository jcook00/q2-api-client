from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.mobile_ws_endpoints import LoginEndpoint


class LoginClient(BaseQ2Client):

    def login_csr(self, request_body):
        """POST /mobilews/logincsr

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = LoginEndpoint.LOGIN_CSR.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def login_user(self, request_body):
        """POST /mobilews/logonUser

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = LoginEndpoint.LOGON_USER.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def logout_user(self):
        """GET /mobilews/logoffUser

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = LoginEndpoint.LOGOFF_USER.value
        return self._get(url=self._build_url(endpoint))
