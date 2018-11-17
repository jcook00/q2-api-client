from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import SecurityEndpoint


class SecurityClient(BaseQ2Client):

    def change_password(self, **request_body):
        endpoint = SecurityEndpoint.CHANGE_PASSWORD.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def validate_password(self, **request_body):
        endpoint = SecurityEndpoint.VALIDATE_PASSWORD.value
        return self._post(url=self._build_url(endpoint), json=request_body)
