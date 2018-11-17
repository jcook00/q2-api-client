from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import LoginEndpoint


class LoginClient(BaseQ2Client):

    def login_csr(self, **request_body):
        endpoint = LoginEndpoint.LOGIN_CSR.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def login_user(self, **request_body):
        endpoint = LoginEndpoint.LOGON_USER.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def logout_user(self):
        endpoint = LoginEndpoint.LOGOFF_USER.value
        return self._get(url=self._build_url(endpoint))
