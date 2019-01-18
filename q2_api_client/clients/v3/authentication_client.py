from q2_api_client.clients.base_q2_client import BaseQ2Client
from q2_api_client.endpoints.v3_endpoints import AuthenticationEndpoint


class AuthenticationClient(BaseQ2Client):

    def keep_alive(self):
        """GET /v3/keepalive

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AuthenticationEndpoint.KEEP_ALIVE.value
        return self._get(url=self._build_url(endpoint))

    def login(self, request_body, csr_assist=None):
        """POST /v3/login

        :param float csr_assist: query parameter
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AuthenticationEndpoint.LOGIN.value
        query_parameters = self._copy_query_parameters()
        query_parameters['csrassist'] = csr_assist
        return self._post(url=self._build_url(endpoint), json=request_body, query_parameters=query_parameters)

    def logoff(self):
        """POST /v3/logoff

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AuthenticationEndpoint.LOGOFF.value
        return self._post(url=self._build_url(endpoint))

    def mfa_login(self, device_key, request_body):
        """POST /v3/mfaLogin

        :param str device_key: header
        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AuthenticationEndpoint.MFA_LOGIN.value
        headers = self._copy_headers()
        headers['deviceKey'] = device_key
        return self._post(url=self._build_url(endpoint), json=request_body, headers=headers)

    def pre_login(self, request_body):
        """POST /v3/preLogin

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AuthenticationEndpoint.PRE_LOGIN.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def register_device(self):
        """POST /v3/registerDevice

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AuthenticationEndpoint.REGISTER_DEVICE.value
        return self._post(url=self._build_url(endpoint))

    def retrieve_status(self):
        """POST /v3/retrieveStatus

        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AuthenticationEndpoint.RETRIEVE_STATUS.value
        return self._post(url=self._build_url(endpoint))

    def validate_mfa(self, request_body):
        """POST /v3/validateMfa

        :param dict request_body: Dictionary object to send in the body of the request
        :return: Response object
        :rtype: requests.Response
        """
        endpoint = AuthenticationEndpoint.VALIDATE_MFA.value
        return self._post(url=self._build_url(endpoint), json=request_body)
