from client.clients.base_q2_client import BaseQ2Client
from client.endpoints.mobile_ws_endpoints import CSREndpoint


class CSRClient(BaseQ2Client):

    def update_csr_config(self, **request_body):
        endpoint = CSREndpoint.CONFIG.value
        return self._put(url=self._build_url(endpoint), json=request_body)

    def get_csr_config(self, name):
        endpoint = CSREndpoint.CONFIG_NAME.value.format(name=name)
        return self._get(url=self._build_url(endpoint))

    def get_csr_config_with_prefix(self, name, prefix):
        endpoint = CSREndpoint.CONFIG_PREFIXED.value.format(name=name, prefixNameWithLoginDot=prefix)
        return self._get(url=self._build_url(endpoint))

    def get_dashboard_activity(self):
        endpoint = CSREndpoint.DASHBOARD_ACTIVITY.value
        return self._get(url=self._build_url(endpoint))

    def get_csr_navigation(self):
        endpoint = CSREndpoint.NAV.value
        return self._get(url=self._build_url(endpoint))

    def get_csr_properties(self):
        endpoint = CSREndpoint.PROPERTIES.value
        return self._get(url=self._build_url(endpoint))
