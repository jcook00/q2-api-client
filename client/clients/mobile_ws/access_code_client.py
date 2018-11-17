from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import AccessCodeEndpoint


class AccessCodeClient(BaseQ2Client):

    def create_access_code(self, **request_body):
        endpoint = AccessCodeEndpoint.ACCESS_CODE.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def validate_access_code(self, **request_body):
        endpoint = AccessCodeEndpoint.ACCESS_CODE_VALIDATE.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def validate_access_code_token(self, **request_body):
        endpoint = AccessCodeEndpoint.ACCESS_CODE_VALIDATE_TOKEN.value
        return self._post(url=self._build_url(endpoint), json=request_body)