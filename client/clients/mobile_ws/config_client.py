from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import ConfigEndpoint


class ConfigClient(BaseQ2Client):

    def get_uux_configuration(self):
        endpoint = ConfigEndpoint.UUX_CONFIGURATION.value
        return self._get(url=self._build_url(endpoint))

    def delete_uux_configuration(self):
        endpoint = ConfigEndpoint.UUX_CONFIGURATION.value
        return self._delete(url=self._build_url(endpoint))

    def create_uux_configuration(self, **request_body):
        endpoint = ConfigEndpoint.UUX_CONFIGURATION.value
        return self._post(url=self._build_url(endpoint), json=request_body)

    def update_uux_configuration(self, **request_body):
        endpoint = ConfigEndpoint.UUX_CONFIGURATION.value
        return self._put(url=self._build_url(endpoint), json=request_body)
